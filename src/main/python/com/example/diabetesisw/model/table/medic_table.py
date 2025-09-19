from typing import Optional
import sqlite3
from .sql_table import SQLTable
from ..type.medic import Medic
from .tables_type import TablesType

class MedicTable(SQLTable[Medic]):
    def __init__(self):
        super().__init__(TablesType.MEDIC.value)

    def getFromResultSet(self, row: sqlite3.Row) -> Medic:
        return Medic.getFromResultSet(row)

    def findAuthorized(self, email: str, password: str) -> Optional[Medic]:
        for medic in self.observable_list:
            if medic.getEmail() == email.lower() and medic.getPassword() == password:
                return medic
        return None