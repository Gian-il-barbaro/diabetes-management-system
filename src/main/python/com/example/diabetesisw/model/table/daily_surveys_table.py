from typing import List
from datetime import date
import sqlite3
from .sql_table import SQLTable
from ..type.daily_surveys import DailySurveys
from ..type.patient import Patient
from .tables_type import TablesType

class DailySurveysTable(SQLTable[DailySurveys]):
    def __init__(self):
        super().__init__(TablesType.DAILYSURVEYS.value)

    def getFromResultSet(self, row: sqlite3.Row) -> DailySurveys:
        return DailySurveys.getFromResultSet(row)

    def getDailySurveysFromPatient(self, patient: Patient) -> List[DailySurveys]:
        return [ds for ds in self.observable_list if ds.getPatientId() == patient.getId()]

    def getDailySurveysFromPatientAndPeriod(self, patient: Patient, start_date: date, end_date: date) -> List[DailySurveys]:
        patient_surveys = self.getDailySurveysFromPatient(patient)
        return [ds for ds in patient_surveys if start_date <= ds.getDate() <= end_date]

    def getLatestDailySurvey(self, patient: Patient) -> DailySurveys:
        patient_surveys = self.getDailySurveysFromPatient(patient)
        if not patient_surveys:
            return None
        return max(patient_surveys, key=lambda ds: ds.getDate())