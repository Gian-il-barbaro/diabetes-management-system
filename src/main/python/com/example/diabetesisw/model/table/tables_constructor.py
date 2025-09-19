from .tables_type import TablesType

class TablesConstructor:
    @staticmethod
    def getTableConstructor(table_type: str) -> str:
        table_type_enum = TablesType(table_type.upper())

        if table_type_enum == TablesType.ALERT:
            return """(
                alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
                medic_id INTEGER NOT NULL,
                patient_id INTEGER NOT NULL,
                description TEXT NOT NULL,
                medic_read BOOLEAN NOT NULL,
                patient_read BOOLEAN NOT NULL,
                alert_type INTEGER NOT NULL,
                date DATE NOT NULL,
                FOREIGN KEY (medic_id) REFERENCES medic(medic_id),
                FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
            )"""

        elif table_type_enum == TablesType.DAILYSURVEYS:
            return """(
                ds_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                fasting_glucose INTEGER NOT NULL,
                post_meal_glucose INTEGER NOT NULL,
                tk_ids TEXT DEFAULT '[]',
                symptom_ids TEXT DEFAULT '[]',
                date DATE NOT NULL,
                FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
            )"""

        elif table_type_enum == TablesType.MEDIC:
            return """(
                medic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )"""

        elif table_type_enum == TablesType.PATIENT:
            return """(
                patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                medic_id INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                password TEXT NOT NULL,
                risk_factors TEXT DEFAULT '[]',
                previous_diseases TEXT DEFAULT '[]',
                comorbidity TEXT DEFAULT '[]',
                FOREIGN KEY (medic_id) REFERENCES medic(medic_id)
            )"""

        elif table_type_enum == TablesType.SYMPTOMS:
            return """(
                symptom_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                ds_id INTEGER NOT NULL,
                from_date DATE NOT NULL,
                to_date DATE NOT NULL,
                description TEXT NOT NULL,
                FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
                FOREIGN KEY (ds_id) REFERENCES dailysurveys(ds_id)
            )"""

        elif table_type_enum == TablesType.TAKINGDRUG:
            return """(
                tk_id INTEGER PRIMARY KEY AUTOINCREMENT,
                ds_id INTEGER NOT NULL,
                patient_id INTEGER NOT NULL,
                drug TEXT NOT NULL,
                date DATE NOT NULL,
                qty REAL NOT NULL,
                FOREIGN KEY (ds_id) REFERENCES dailysurveys(ds_id),
                FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
            )"""

        elif table_type_enum == TablesType.THERAPY:
            return """(
                therapy_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                drug TEXT NOT NULL,
                qty_intake_drug REAL NOT NULL,
                daily_intake INTEGER NOT NULL,
                start_date DATE NOT NULL,
                end_date DATE,
                FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
            )"""

        else:
            raise ValueError(f"Unknown table type: {table_type}")