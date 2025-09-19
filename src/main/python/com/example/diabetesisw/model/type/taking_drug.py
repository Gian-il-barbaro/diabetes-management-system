from typing import List, Dict, Any
from datetime import date
import sqlite3
from .general_type import GeneralType

class TakingDrug(GeneralType):
    STRING_ID = "tk_id"

    def __init__(self, ds_id: int = None, patient_id: int = None, drug: str = "",
                 date: date = None, qty: float = 0.0, tk_id: int = -1):
        self._tk_id = tk_id
        self._ds_id = ds_id
        self._patient_id = patient_id
        self._drug = drug
        self._date = date
        self._qty = self._round(qty, 4)

    @classmethod
    def from_constructor(cls, ds_id: int, patient_id: int, drug: str, date: date, qty: float) -> 'TakingDrug':
        return cls(ds_id, patient_id, drug, date, qty)

    @classmethod
    def from_db(cls, tk_id: int, ds_id: int, patient_id: int, drug: str, date: date, qty: float) -> 'TakingDrug':
        return cls(ds_id, patient_id, drug, date, qty, tk_id)

    @staticmethod
    def getFromResultSet(row: sqlite3.Row) -> 'TakingDrug':
        return TakingDrug.from_db(
            row["tk_id"],
            row["ds_id"],
            row["patient_id"],
            row["drug"],
            row["date"],
            row["qty"]
        )

    @staticmethod
    def _round(value: float, places: int) -> float:
        if places < 0:
            raise ValueError("Places must be non-negative")
        factor = 10 ** places
        return round(value * factor) / factor

    def takingDrugIdProperty(self) -> int:
        return self._tk_id

    def getDailySurveysId(self) -> int:
        return self._ds_id

    def setDailySurveysId(self, ds_id: int) -> None:
        self._ds_id = ds_id

    def dailySurveysIdProperty(self) -> int:
        return self._ds_id

    def getPatientId(self) -> int:
        return self._patient_id

    def patientIdProperty(self) -> int:
        return self._patient_id

    def getDrug(self) -> str:
        return self._drug

    def setDrug(self, drug: str) -> None:
        self._drug = drug

    def drugProperty(self) -> str:
        return self._drug

    def getDate(self) -> date:
        return self._date

    def setDate(self, date: date) -> None:
        self._date = date

    def dateProperty(self) -> date:
        return self._date

    def getQty(self) -> float:
        return self._qty

    def setQty(self, qty: float) -> None:
        self._qty = self._round(qty, 4)

    def qtyProperty(self) -> float:
        return self._qty

    def copyWithDiffId(self, id: int) -> 'TakingDrug':
        return TakingDrug.from_db(id, self._ds_id, self._patient_id, self._drug, self._date, self._qty)

    def getId(self) -> int:
        return self._tk_id

    def getStringId(self) -> str:
        return self.STRING_ID

    def getProperties(self) -> List[Any]:
        return [
            self._ds_id,
            self._patient_id,
            self._drug,
            self._date,
            self._qty
        ]

    def getPropertiesType(self) -> Dict[Any, str]:
        return {
            self._ds_id: int.__name__,
            self._patient_id: int.__name__,
            self._drug: str.__name__,
            self._date: date.__name__,
            self._qty: float.__name__
        }