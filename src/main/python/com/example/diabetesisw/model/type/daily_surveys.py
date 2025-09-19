from typing import List, Dict, Any
from datetime import date
import sqlite3
from .general_type import GeneralType
from ...utils.properties.string_list_property import StringListProperty

class DailySurveys(GeneralType):
    STRING_ID = "ds_id"

    def __init__(self, patient_id: int = None, fasting_glucose: int = 0, post_meal_glucose: int = 0,
                 date: date = None, ds_id: int = -1, tk_ids: str = "[]", symptom_ids: str = "[]"):
        self._ds_id = ds_id
        self._patient_id = patient_id
        self._fasting_glucose = fasting_glucose
        self._post_meal_glucose = post_meal_glucose
        self._tk_ids = StringListProperty(int, self, "tk_ids")
        self._symptom_ids = StringListProperty(int, self, "symptom_ids")
        self._date = date

        self._tk_ids.set(tk_ids)
        self._symptom_ids.set(symptom_ids)

    @classmethod
    def from_constructor(cls, patient_id: int, fasting_glucose: int, post_meal_glucose: int, date: date) -> 'DailySurveys':
        return cls(patient_id, fasting_glucose, post_meal_glucose, date)

    @classmethod
    def from_db(cls, ds_id: int, patient_id: int, fasting_glucose: int, post_meal_glucose: int,
                tk_ids: str, symptoms_ids: str, date: date) -> 'DailySurveys':
        return cls(patient_id, fasting_glucose, post_meal_glucose, date, ds_id, tk_ids, symptoms_ids)

    @staticmethod
    def getFromResultSet(row: sqlite3.Row) -> 'DailySurveys':
        return DailySurveys.from_db(
            row["ds_id"],
            row["patient_id"],
            row["fasting_glucose"],
            row["post_meal_glucose"],
            row["tk_ids"],
            row["symptom_ids"],
            row["date"]
        )

    def dailySurveysIdProperty(self) -> int:
        return self._ds_id

    def getPatientId(self) -> int:
        return self._patient_id

    def patientIdProperty(self) -> int:
        return self._patient_id

    def getFastingGlucose(self) -> int:
        return self._fasting_glucose

    def setFastingGlucose(self, fasting_glucose: int) -> None:
        self._fasting_glucose = fasting_glucose

    def fastingGlucoseProperty(self) -> int:
        return self._fasting_glucose

    def getPostMealGlucose(self) -> int:
        return self._post_meal_glucose

    def setPostMealGlucose(self, post_meal_glucose: int) -> None:
        self._post_meal_glucose = post_meal_glucose

    def postMealGlucoseProperty(self) -> int:
        return self._post_meal_glucose

    def putTakingDrug(self, drug: str, date: date, qty: float) -> 'TakingDrug':
        from ..model import Model
        from .taking_drug import TakingDrug
        tk = Model.getInstance().takingDrugTable().insert(
            TakingDrug(self.getId(), self.getPatientId(), drug, date, qty)
        )
        self.listTkIdsProperty().add(tk.getId())
        return tk

    def listTkIdsProperty(self) -> StringListProperty[int]:
        return self._tk_ids

    def putSymptom(self, from_date: date, to_date: date, description: str) -> 'Symptom':
        from ..model import Model
        from .symptom import Symptom
        symptom = Model.getInstance().symptomsTable().insert(
            Symptom(self.getPatientId(), self.getId(), from_date, to_date, description)
        )
        self.listSymptomIdsProperty().add(symptom.getId())
        return symptom

    def listSymptomIdsProperty(self) -> StringListProperty[int]:
        return self._symptom_ids

    def dateProperty(self) -> date:
        return self._date

    def getDate(self) -> date:
        return self._date

    def setDate(self, date: date) -> None:
        self._date = date

    def copyWithDiffId(self, id: int) -> 'DailySurveys':
        return DailySurveys.from_db(
            id,
            self._patient_id,
            self._fasting_glucose,
            self._post_meal_glucose,
            self._tk_ids.stringProperty().get(),
            self._symptom_ids.stringProperty().get(),
            self._date
        )

    def getId(self) -> int:
        return self._ds_id

    def getStringId(self) -> str:
        return self.STRING_ID

    def getProperties(self) -> List[Any]:
        return [
            self._patient_id,
            self._fasting_glucose,
            self._post_meal_glucose,
            self._tk_ids,
            self._symptom_ids,
            self._date
        ]

    def getPropertiesType(self) -> Dict[Any, str]:
        return {
            self._patient_id: int.__name__,
            self._fasting_glucose: int.__name__,
            self._post_meal_glucose: int.__name__,
            self._tk_ids: str.__name__,
            self._symptom_ids: str.__name__,
            self._date: date.__name__
        }