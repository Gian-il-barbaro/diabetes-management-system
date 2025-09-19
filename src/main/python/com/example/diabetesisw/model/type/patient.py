from typing import List, Dict, Any, Optional
from datetime import date
import sqlite3
from .general_type import GeneralType
from ...utils.string_utils import StringUtils
from ...utils.properties.string_list_property import StringListProperty

class Patient(GeneralType):
    STRING_ID = "patient_id"

    def __init__(self, medic_id: int = None, email: str = "", name: str = "", surname: str = "",
                 password: str = "", risk_factors: List[str] = None, previous_diseases: List[str] = None,
                 comorbidity: List[str] = None, patient_id: int = -1):
        self._patient_id = patient_id
        self._medic_id_ref = medic_id
        self._email = email.lower() if email else ""
        self._name = name
        self._surname = surname
        self._password = password
        self._risk_factors = StringListProperty(str, self, "risk_factors")
        self._previous_diseases = StringListProperty(str, self, "previous_diseases")
        self._comorbidity = StringListProperty(str, self, "comorbidity")

        if risk_factors:
            self._risk_factors.addAll(risk_factors)
        if previous_diseases:
            self._previous_diseases.addAll(previous_diseases)
        if comorbidity:
            self._comorbidity.addAll(comorbidity)

    @classmethod
    def from_constructor(cls, medic_id: int, email: str, name: str, surname: str,
                        password: str, risk_factors: List[str], previous_diseases: List[str],
                        comorbidity: List[str]) -> 'Patient':
        return cls(medic_id, email, name, surname, password, risk_factors, previous_diseases, comorbidity)

    @classmethod
    def from_db(cls, patient_id: int, medic_id: int, email: str, name: str, surname: str,
                password: str, risk_factors: str, previous_diseases: str, comorbidity: str) -> 'Patient':
        patient = cls(medic_id, email, name, surname, password, patient_id=patient_id)
        patient._risk_factors.set(risk_factors)
        patient._previous_diseases.set(previous_diseases)
        patient._comorbidity.set(comorbidity)
        return patient

    @staticmethod
    def getFromResultSet(row: sqlite3.Row) -> 'Patient':
        return Patient.from_db(
            row["patient_id"],
            row["medic_id"],
            row["email"],
            row["name"],
            row["surname"],
            row["password"],
            row["risk_factors"],
            row["previous_diseases"],
            row["comorbidity"]
        )

    def patientIdProperty(self) -> int:
        return self._patient_id

    def getMedicId(self) -> int:
        return self._medic_id_ref

    def medicIdRefProperty(self) -> int:
        return self._medic_id_ref

    def getEmail(self) -> str:
        return self._email

    def emailProperty(self) -> str:
        return self._email

    def setEmail(self, email: str) -> None:
        self._email = email.lower()

    def getFullName(self) -> str:
        return f"{self.getName()} {self.getSurname()}"

    def getFullNameCapitalized(self) -> str:
        return f"{StringUtils.capitalize(self.getName())} {StringUtils.capitalize(self.getSurname())}"

    def getName(self) -> str:
        return self._name

    def setName(self, name: str) -> None:
        self._name = name

    def nameProperty(self) -> str:
        return self._name

    def getSurname(self) -> str:
        return self._surname

    def setSurname(self, surname: str) -> None:
        self._surname = surname

    def surnameProperty(self) -> str:
        return self._surname

    def getPassword(self) -> str:
        return self._password

    def setPassword(self, password: str) -> None:
        self._password = password

    def passwordProperty(self) -> str:
        return self._password

    def listRiskFactorsProperty(self) -> StringListProperty[str]:
        return self._risk_factors

    def listPreviousDiseasesProperty(self) -> StringListProperty[str]:
        return self._previous_diseases

    def listComorbidityProperty(self) -> StringListProperty[str]:
        return self._comorbidity

    def createDailySurveys(self, fasting_glucose: int, post_meal_glucose: int, date: date) -> 'DailySurveys':
        from ..model import Model
        from .daily_surveys import DailySurveys
        return Model.getInstance().dailySurveysTable().insert(
            DailySurveys(self.getId(), fasting_glucose, post_meal_glucose, date)
        )

    def copyWithDiffId(self, id: int) -> 'Patient':
        return Patient.from_db(
            id,
            self._medic_id_ref,
            self._email,
            self._name,
            self._surname,
            self._password,
            self._risk_factors.stringProperty().get(),
            self._previous_diseases.stringProperty().get(),
            self._comorbidity.stringProperty().get()
        )

    def getId(self) -> int:
        return self._patient_id

    def getStringId(self) -> str:
        return self.STRING_ID

    def getProperties(self) -> List[Any]:
        return [
            self._medic_id_ref,
            self._email,
            self._name,
            self._surname,
            self._password,
            self._risk_factors,
            self._previous_diseases,
            self._comorbidity
        ]

    def getPropertiesType(self) -> Dict[Any, str]:
        return {
            self._medic_id_ref: int.__name__,
            self._email: str.__name__,
            self._name: str.__name__,
            self._surname: str.__name__,
            self._password: str.__name__,
            self._risk_factors: str.__name__,
            self._previous_diseases: str.__name__,
            self._comorbidity: str.__name__
        }