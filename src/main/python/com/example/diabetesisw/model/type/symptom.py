from typing import List, Dict, Any
from datetime import date
import sqlite3
from .general_type import GeneralType

class Symptom(GeneralType):
    STRING_ID = "symptom_id"

    def __init__(self, patient_id: int = None, ds_id: int = None, from_date: date = None,
                 to_date: date = None, description: str = "", symptom_id: int = -1):
        self._symptom_id = symptom_id
        self._patient_id = patient_id
        self._ds_id = ds_id
        self._from = from_date
        self._to = to_date
        self._description = description

    @classmethod
    def from_constructor(cls, patient_id: int, ds_id: int, from_date: date, to_date: date, description: str) -> 'Symptom':
        return cls(patient_id, ds_id, from_date, to_date, description)

    @classmethod
    def from_db(cls, symptom_id: int, patient_id: int, ds_id: int, from_date: date, to_date: date, description: str) -> 'Symptom':
        return cls(patient_id, ds_id, from_date, to_date, description, symptom_id)

    @staticmethod
    def getFromResultSet(row: sqlite3.Row) -> 'Symptom':
        return Symptom.from_db(
            row["symptom_id"],
            row["patient_id"],
            row["ds_id"],
            row["from_date"],
            row["to_date"],
            row["description"]
        )

    def symptomIdProperty(self) -> int:
        return self._symptom_id

    def getPatientId(self) -> int:
        return self._patient_id

    def patientIdProperty(self) -> int:
        return self._patient_id

    def setPatientId(self, patient_id: int) -> None:
        self._patient_id = patient_id

    def getDailySurveyId(self) -> int:
        return self._ds_id

    def dailySurveyIdProperty(self) -> int:
        return self._ds_id

    def setDailySurveyId(self, ds_id: int) -> None:
        self._ds_id = ds_id

    def getFrom(self) -> date:
        return self._from

    def fromProperty(self) -> date:
        return self._from

    def setFrom(self, from_date: date) -> None:
        self._from = from_date

    def getTo(self) -> date:
        return self._to

    def toProperty(self) -> date:
        return self._to

    def setTo(self, to_date: date) -> None:
        self._to = to_date

    def getDescription(self) -> str:
        return self._description

    def descriptionProperty(self) -> str:
        return self._description

    def setDescription(self, description: str) -> None:
        self._description = description

    def copyWithDiffId(self, id: int) -> 'Symptom':
        return Symptom.from_db(id, self._patient_id, self._ds_id, self._from, self._to, self._description)

    def getId(self) -> int:
        return self._symptom_id

    def getStringId(self) -> str:
        return self.STRING_ID

    def getProperties(self) -> List[Any]:
        return [
            self._patient_id,
            self._ds_id,
            self._from,
            self._to,
            self._description
        ]

    def getPropertiesType(self) -> Dict[Any, str]:
        return {
            self._patient_id: int.__name__,
            self._ds_id: int.__name__,
            self._from: date.__name__,
            self._to: date.__name__,
            self._description: str.__name__
        }