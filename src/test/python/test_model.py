import unittest
import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'main', 'python'))

from com.example.diabetesisw.model.model import Model
from com.example.diabetesisw.model.type.medic import Medic

class TestModel(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix='.sqlite', delete=False)
        self.temp_db.close()

        Model.DB_PATH = self.temp_db.name
        self.model = Model.getInstance()

    def tearDown(self):
        self.model.close()
        try:
            os.unlink(self.temp_db.name)
        except:
            pass

    def test_database_connection(self):
        self.model.connect()
        self.assertIsNotNone(self.model.connection)
        self.model.disconnect()
        self.assertIsNone(self.model.connection)

    def test_table_creation(self):
        self.model.connect()
        medic_table = self.model.medicTable()

        self.assertFalse(medic_table.exist())
        medic_table.createTable()
        self.assertTrue(medic_table.exist())

    def test_medic_insertion(self):
        self.model.connect()
        medic_table = self.model.medicTable()
        medic_table.createTable()

        medic = Medic.from_constructor("Mario", "Rossi", "mario@test.com", "password")
        inserted_medic = medic_table.insert(medic)

        self.assertNotEqual(inserted_medic.getId(), -1)
        self.assertEqual(inserted_medic.getName(), "Mario")

if __name__ == '__main__':
    unittest.main()