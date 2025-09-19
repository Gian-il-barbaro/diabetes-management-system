from typing import List
import sqlite3
from .sql_table import SQLTable
from ..type.alert import Alert
from ..type.patient import Patient
from .tables_type import TablesType

class AlertTable(SQLTable[Alert]):
    def __init__(self):
        super().__init__(TablesType.ALERT.value)

    def getFromResultSet(self, row: sqlite3.Row) -> Alert:
        return Alert.getFromResultSet(row)

    def getAllPatientAlert(self, patient: Patient) -> List[Alert]:
        return [alert for alert in self.observable_list if alert.getPatientId() == patient.getId()]

    def getAllMedicAlert(self, medic_id: int) -> List[Alert]:
        return [alert for alert in self.observable_list if alert.getMedicId() == medic_id]

    def getUnreadPatientAlerts(self, patient: Patient) -> List[Alert]:
        return [alert for alert in self.getAllPatientAlert(patient) if not alert.isPatientRead()]

    def getUnreadMedicAlerts(self, medic_id: int) -> List[Alert]:
        return [alert for alert in self.getAllMedicAlert(medic_id) if not alert.isMedicRead()]