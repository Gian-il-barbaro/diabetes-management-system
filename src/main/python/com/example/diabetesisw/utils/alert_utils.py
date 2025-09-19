from typing import List
from datetime import date, timedelta
from ..model.type.patient import Patient
from ..model.type.alert import Alert
from ..model.type.taking_drug import TakingDrug
from ..model.type.therapy import Therapy
from ..utils.date_utils import DateUtils

class AlertUtils:
    DAY_IN_MS = 24 * 60 * 60 * 1000

    @staticmethod
    def checkPatientAlerts(patient: Patient) -> None:
        AlertUtils.checkIfPatientSubmittedRecently(patient)

        from ..model.model import Model
        patient_therapies = Model.getInstance().therapyTable().getTherapyOfPatients(patient)

        yesterday = date.today() - timedelta(days=1)
        for therapy in patient_therapies:
            AlertUtils.checkPatientDosesForDay(patient, therapy, yesterday)

        AlertUtils.garbageCollector()

    @staticmethod
    def checkIfPatientSubmittedRecently(patient: Patient) -> None:
        from ..model.model import Model
        model = Model.getInstance()

        yesterday = date.today() - timedelta(days=1)
        today = date.today()

        daily_surveys_list = model.dailySurveysTable().getDailySurveysFromPatientAndPeriod(
            patient, yesterday, today
        )

        if daily_surveys_list:
            return

        existing_alerts = model.alertTable().getAllPatientAlert(patient)
        inactivity_alerts = [alert for alert in existing_alerts if alert.getAlertType() == Alert.Type.Inactivity]

        if inactivity_alerts:
            for alert in inactivity_alerts:
                alert.setMedicRead(False)
                alert.setPatientRead(False)
            return

        model.alertTable().insert(Alert.from_constructor(
            patient.getMedicId(),
            patient.getId(),
            "inserito dati per più di 3 giorni consecutivi",
            False,
            False,
            Alert.Type.Inactivity,
            date.today()
        ))

    @staticmethod
    def checkIfPatientFollowsPrescription(patient: Patient, taking_drug: TakingDrug, check_date: date) -> None:
        from ..model.model import Model
        model = Model.getInstance()

        therapy = model.therapyTable().getTherapyOfPatientByName(patient, taking_drug.getDrug())

        if therapy.getQtyIntakeDrug() != taking_drug.getQty():
            model.alertTable().insert(Alert.from_constructor(
                patient.getMedicId(),
                patient.getId(),
                f"assunto {taking_drug.getQty()} mg di {taking_drug.getDrug()}, invece di {therapy.getQtyIntakeDrug()} mg",
                False,
                False,
                Alert.Type.WrongDrug,
                check_date
            ))

        patient_drugs = model.takingDrugTable().getTakingDrugFromPatient(patient)
        same_day_drugs = [drug for drug in patient_drugs if DateUtils.isSameDay(drug.getDate(), check_date)]
        sum_of_doses = sum(drug.getQty() for drug in same_day_drugs)

        description = f"assunto {sum_of_doses} mg di {taking_drug.getDrug()} come dose totale giornaliera, invece di {therapy.getDailyIntake() * therapy.getQtyIntakeDrug()} mg"

        existing_alerts = model.alertTable().getAllPatientAlert(patient)
        too_much_drug_alerts = [
            alert for alert in existing_alerts
            if alert.getAlertType() == Alert.Type.TooMuchDrug and DateUtils.isSameDay(alert.getDate(), check_date)
        ]

        for alert in too_much_drug_alerts:
            model.alertTable().remove(alert)

        if sum_of_doses > therapy.getDailyIntake() * therapy.getQtyIntakeDrug():
            model.alertTable().insert(Alert.from_constructor(
                patient.getMedicId(),
                patient.getId(),
                description,
                False,
                False,
                Alert.Type.TooMuchDrug,
                check_date
            ))

    @staticmethod
    def checkPatientDosesForDay(patient: Patient, therapy: Therapy, check_date: date) -> None:
        from ..model.model import Model
        model = Model.getInstance()

        existing_alerts = model.alertTable().getAllPatientAlert(patient)
        too_little_drug_alerts = [
            alert for alert in existing_alerts
            if alert.getAlertType() == Alert.Type.TooLittleDrug and DateUtils.isSameDay(alert.getDate(), check_date)
        ]

        if too_little_drug_alerts:
            return

        patient_drugs = model.takingDrugTable().getTakingDrugFromPatient(patient)
        same_day_drugs = [drug for drug in patient_drugs if DateUtils.isSameDay(drug.getDate(), check_date)]
        sum_of_doses = sum(drug.getQty() for drug in same_day_drugs)

        if sum_of_doses < therapy.getDailyIntake() * therapy.getQtyIntakeDrug():
            model.alertTable().insert(Alert.from_constructor(
                patient.getMedicId(),
                patient.getId(),
                f"assunto {sum_of_doses} mg di {therapy.getDrug()} come dose totale giornaliera, invece di {therapy.getDailyIntake() * therapy.getQtyIntakeDrug()} mg",
                False,
                False,
                Alert.Type.TooLittleDrug,
                check_date
            ))

    @staticmethod
    def patientActive(patient: Patient) -> None:
        from ..model.model import Model
        model = Model.getInstance()

        existing_alerts = model.alertTable().getAllPatientAlert(patient)
        inactivity_alerts = [alert for alert in existing_alerts if alert.getAlertType() == Alert.Type.Inactivity]

        for alert in inactivity_alerts:
            model.alertTable().remove(alert)

    @staticmethod
    def checkPatientGlucoseLevel(patient: Patient, fasting_glucose: int, post_meal_glucose: int, check_date: date) -> None:
        from ..model.model import Model
        model = Model.getInstance()

        message_header = f"una glicemia a digiuno di {fasting_glucose} mg/dL e post-prandiale di {post_meal_glucose} mg/dL"

        fasting_alert_type = AlertUtils._glucoseRanges(fasting_glucose, 70, 100, 126, 200, 300)
        post_meal_alert_type = AlertUtils._glucoseRanges(post_meal_glucose, 70, 140, 180, 250, 400)

        alert_type = max(fasting_alert_type, post_meal_alert_type, key=lambda x: x.value if x != Alert.Type.WrongDrug else -1)

        if alert_type != Alert.Type.WrongDrug:
            AlertUtils._insertGlucoseAlert(patient, message_header, alert_type, check_date)

    @staticmethod
    def _glucoseRanges(val: int, hypoglycemia: int, normal: int, mild: int, moderate: int, severe: int) -> Alert.Type:
        if val < hypoglycemia:
            return Alert.Type.GlucoseHypoglycemia
        if val < normal:
            return Alert.Type.WrongDrug
        if val < mild:
            return Alert.Type.GlucoseNormHigh
        if val < moderate:
            return Alert.Type.GlucoseMild
        if val < severe:
            return Alert.Type.GlucoseModerate
        return Alert.Type.GlucoseSevere

    @staticmethod
    def _insertGlucoseAlert(patient: Patient, message_header: str, alert_type: Alert.Type, check_date: date) -> None:
        message = message_header

        if alert_type == Alert.Type.GlucoseHypoglycemia:
            message += " (Ipoglicemia)"
        elif alert_type == Alert.Type.GlucoseNormHigh:
            message += " (Glicemia normale-alta)"
        elif alert_type == Alert.Type.GlucoseBorderline:
            message += " (Glicemia borderline)"
        elif alert_type == Alert.Type.GlucoseMild:
            message += " (Iperglicemia lieve)"
        elif alert_type == Alert.Type.GlucoseModerate:
            message += " (Iperglicemia moderata)"
        elif alert_type == Alert.Type.GlucoseSevere:
            message += " (Iperglicemia grave)"
        elif alert_type == Alert.Type.GlucoseHyperglycemia:
            message += " (Iperglicemia severa)"

        from ..model.model import Model
        Model.getInstance().alertTable().insert(Alert.from_constructor(
            patient.getMedicId(),
            patient.getId(),
            message,
            False,
            False,
            alert_type,
            check_date
        ))

    @staticmethod
    def garbageCollector() -> None:
        from ..model.model import Model
        model = Model.getInstance()

        alerts_to_remove = [
            alert for alert in model.alertTable().toList()
            if alert.isMedicRead() and alert.isPatientRead()
        ]

        for alert in alerts_to_remove:
            model.alertTable().remove(alert)