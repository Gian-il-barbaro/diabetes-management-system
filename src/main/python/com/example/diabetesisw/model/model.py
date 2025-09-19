from typing import Optional, List, Any, Tuple
import sqlite3
import os
from .table.patient_table import PatientTable
from .table.medic_table import MedicTable
from .table.alert_table import AlertTable
from .table.daily_surveys_table import DailySurveysTable

class Model:
    _instance: Optional['Model'] = None
    DB_PATH = "diabetes_database.sqlite"

    def __init__(self):
        self.connection: Optional[sqlite3.Connection] = None
        self._patient_table: Optional[PatientTable] = None
        self._medic_table: Optional[MedicTable] = None
        self._alert_table: Optional[AlertTable] = None
        self._daily_surveys_table: Optional[DailySurveysTable] = None

    @classmethod
    def getInstance(cls) -> 'Model':
        if cls._instance is None:
            cls._instance = Model()
        return cls._instance

    def connect(self) -> None:
        try:
            self.connection = sqlite3.connect(self.DB_PATH)
            self.connection.row_factory = sqlite3.Row
            print(f"Connected to database: {self.DB_PATH}")
        except Exception as e:
            raise RuntimeError(f"Failed to connect to database: {e}")

    def disconnect(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Database connection closed")

    def hasTable(self, table_name: str) -> bool:
        if not self.connection:
            raise RuntimeError("Database not connected")

        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name=?
        """, (table_name,))

        return cursor.fetchone() is not None

    def runStatement(self, statement: str, parameters: Tuple = ()) -> None:
        if not self.connection:
            raise RuntimeError("Database not connected")

        try:
            cursor = self.connection.cursor()
            cursor.execute(statement, parameters)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise RuntimeError(f"Failed to execute statement: {e}")

    def query(self, query: str, parameters: Tuple = ()) -> List[sqlite3.Row]:
        if not self.connection:
            raise RuntimeError("Database not connected")

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, parameters)
            return cursor.fetchall()
        except Exception as e:
            raise RuntimeError(f"Failed to execute query: {e}")

    def insert(self, table_name: str, columns: str, values: str) -> int:
        if not self.connection:
            raise RuntimeError("Database not connected")

        try:
            statement = f"INSERT INTO {table_name} {columns} VALUES {values}"
            cursor = self.connection.cursor()
            cursor.execute(statement)
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            self.connection.rollback()
            raise RuntimeError(f"Failed to insert into {table_name}: {e}")

    def update(self, table_name: str, set_clause: str, where_clause: str) -> None:
        if not self.connection:
            raise RuntimeError("Database not connected")

        try:
            statement = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            cursor = self.connection.cursor()
            cursor.execute(statement)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise RuntimeError(f"Failed to update {table_name}: {e}")

    def patientTable(self) -> PatientTable:
        if self._patient_table is None:
            self._patient_table = PatientTable()
        return self._patient_table

    def medicTable(self) -> MedicTable:
        if self._medic_table is None:
            self._medic_table = MedicTable()
        return self._medic_table

    def alertTable(self) -> AlertTable:
        if self._alert_table is None:
            self._alert_table = AlertTable()
        return self._alert_table

    def dailySurveysTable(self) -> DailySurveysTable:
        if self._daily_surveys_table is None:
            self._daily_surveys_table = DailySurveysTable()
        return self._daily_surveys_table

    def initializeDatabase(self) -> None:
        self.connect()

        tables = [
            self.medicTable(),
            self.patientTable(),
            self.dailySurveysTable(),
            self.alertTable()
        ]

        for table in tables:
            if not table.exist():
                table.createTable()
                print(f"Created table: {table.getTableName()}")
            table.load()
            print(f"Loaded table: {table.getTableName()}")

    def close(self) -> None:
        self.disconnect()