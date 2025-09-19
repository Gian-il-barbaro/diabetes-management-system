from typing import List, Optional
import sqlite3
from .sql_table import SQLTable
from ..type.patient import Patient
from .tables_type import TablesType

class PatientTable(SQLTable[Patient]):
    def __init__(self):
        super().__init__(TablesType.PATIENT.value)

    def getFromResultSet(self, row: sqlite3.Row) -> Patient:
        return Patient.getFromResultSet(row)

    def findAuthorized(self, email: str, password: str) -> Optional[Patient]:
        for patient in self.observable_list:
            if patient.getEmail() == email.lower() and patient.getPassword() == password:
                return patient
        return None

    def getPatientsOfMedic(self, medic_id: int) -> List[Patient]:
        return [patient for patient in self.observable_list if patient.getMedicId() == medic_id]