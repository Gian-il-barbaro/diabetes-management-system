from typing import List, Dict, Any
from datetime import date
from enum import Enum
import sqlite3
from .general_type import GeneralType

class Alert(GeneralType):
    STRING_ID = "alert_id"

    class Type(Enum):
        Inactivity = 0
        WrongDrug = 1
        TooMuchDrug = 2
        TooLittleDrug = 3
        GlucoseNormHigh = 4
        GlucoseBorderline = 5
        GlucoseMild = 6
        GlucoseModerate = 7
        GlucoseSevere = 8
        GlucoseHypoglycemia = 9
        GlucoseHyperglycemia = 10

    def __init__(self, medic_id: int = None, patient_id: int = None, description: str = "",
                 medic_read: bool = False, patient_read: bool = False, alert_type: Type = None,
                 date: date = None, alert_id: int = -1):
        self._alert_id = alert_id
        self._medic_id = medic_id
        self._patient_id = patient_id
        self._description = description
        self._medic_read = medic_read
        self._patient_read = patient_read
        self._alert_type = alert_type
        self._date = date

    @classmethod
    def from_constructor(cls, medic_id: int, patient_id: int, description: str, medic_read: bool,
                        patient_read: bool, alert_type: Type, date: date) -> 'Alert':
        return cls(medic_id, patient_id, description, medic_read, patient_read, alert_type, date)

    @classmethod
    def from_db(cls, alert_id: int, medic_id: int, patient_id: int, description: str, medic_read: bool,
                patient_read: bool, alert_type: Type, date: date) -> 'Alert':
        return cls(medic_id, patient_id, description, medic_read, patient_read, alert_type, date, alert_id)

    @staticmethod
    def getFromResultSet(row: sqlite3.Row) -> 'Alert':
        return Alert.from_db(
            row["alert_id"],
            row["medic_id"],
            row["patient_id"],
            row["description"],
            bool(row["medic_read"]),
            bool(row["patient_read"]),
            Alert.Type(row["alert_type"]),
            row["date"]
        )

    def alertIdProperty(self) -> int:
        return self._alert_id

    def getMedicId(self) -> int:
        return self._medic_id

    def medicIdProperty(self) -> int:
        return self._medic_id

    def getPatientId(self) -> int:
        return self._patient_id

    def patientIdProperty(self) -> int:
        return self._patient_id

    def getDescription(self) -> str:
        return self._description

    def descriptionProperty(self) -> str:
        return self._description

    def setDescription(self, description: str) -> None:
        self._description = description

    def isMedicRead(self) -> bool:
        return self._medic_read

    def setMedicRead(self, medic_read: bool) -> None:
        self._medic_read = medic_read

    def medicReadProperty(self) -> bool:
        return self._medic_read

    def isPatientRead(self) -> bool:
        return self._patient_read

    def setPatientRead(self, patient_read: bool) -> None:
        self._patient_read = patient_read

    def patientReadProperty(self) -> bool:
        return self._patient_read

    def getAlertType(self) -> Type:
        return self._alert_type

    def alertTypeProperty(self) -> Type:
        return self._alert_type

    def setAlertType(self, alert_type: Type) -> None:
        self._alert_type = alert_type

    def getDate(self) -> date:
        return self._date

    def dateProperty(self) -> date:
        return self._date

    def setDate(self, date: date) -> None:
        self._date = date

    def copyWithDiffId(self, id: int) -> 'Alert':
        return Alert.from_db(id, self._medic_id, self._patient_id, self._description,
                           self._medic_read, self._patient_read, self._alert_type, self._date)

    def getId(self) -> int:
        return self._alert_id

    def getStringId(self) -> str:
        return self.STRING_ID

    def getProperties(self) -> List[Any]:
        return [
            self._medic_id,
            self._patient_id,
            self._description,
            self._medic_read,
            self._patient_read,
            self._alert_type,
            self._date
        ]

    def getPropertiesType(self) -> Dict[Any, str]:
        return {
            self._medic_id: int.__name__,
            self._patient_id: int.__name__,
            self._description: str.__name__,
            self._medic_read: bool.__name__,
            self._patient_read: bool.__name__,
            self._alert_type: Alert.Type.__name__,
            self._date: date.__name__
        }

    def toStringPatient(self) -> str:
        from ..utils.date_utils import DateUtils
        return f"[{DateUtils.getToString(self.getDate())}] " + \
               ("Non hai " if self.getAlertType() == Alert.Type.Inactivity else "Hai ") + \
               self.getDescription()

    def toStringMedic(self) -> str:
        from ..model import Model
        from ..utils.date_utils import DateUtils
        patient = Model.getInstance().patientTable().getFromId(self.getPatientId())
        return f"[{DateUtils.getToString(self.getDate())}] Il paziente {patient.getFullName()}" + \
               (" non ha " if self.getAlertType() == Alert.Type.Inactivity else " ha ") + \
               self.getDescription()