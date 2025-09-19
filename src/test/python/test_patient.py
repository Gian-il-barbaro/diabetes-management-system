import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'main', 'python'))

from com.example.diabetesisw.model.type.patient import Patient

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patient = Patient.from_constructor(
            medic_id=1,
            email="test@example.com",
            name="Mario",
            surname="Rossi",
            password="password123",
            risk_factors=["Obesità", "Sedentarietà"],
            previous_diseases=["Ipertensione"],
            comorbidity=["Dislipidemia"]
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.getMedicId(), 1)
        self.assertEqual(self.patient.getEmail(), "test@example.com")
        self.assertEqual(self.patient.getName(), "Mario")
        self.assertEqual(self.patient.getSurname(), "Rossi")
        self.assertEqual(self.patient.getPassword(), "password123")

    def test_full_name(self):
        self.assertEqual(self.patient.getFullName(), "Mario Rossi")

    def test_email_lowercase(self):
        patient = Patient.from_constructor(1, "TEST@EXAMPLE.COM", "Test", "User", "pass", [], [], [])
        self.assertEqual(patient.getEmail(), "test@example.com")

    def test_risk_factors(self):
        risk_factors = self.patient.listRiskFactorsProperty().get()
        self.assertIn("Obesità", risk_factors)
        self.assertIn("Sedentarietà", risk_factors)

    def test_copy_with_diff_id(self):
        copied = self.patient.copyWithDiffId(5)
        self.assertEqual(copied.getId(), 5)
        self.assertEqual(copied.getName(), self.patient.getName())

if __name__ == '__main__':
    unittest.main()