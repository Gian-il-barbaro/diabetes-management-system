import unittest
import sys
import os
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'main', 'python'))

from com.example.diabetesisw.utils.alert_utils import AlertUtils
from com.example.diabetesisw.model.type.alert import Alert

class TestAlertUtils(unittest.TestCase):
    def test_glucose_ranges_normal(self):
        alert_type = AlertUtils._glucoseRanges(90, 70, 100, 126, 200, 300)
        self.assertEqual(alert_type, Alert.Type.WrongDrug)

    def test_glucose_ranges_high(self):
        alert_type = AlertUtils._glucoseRanges(140, 70, 100, 126, 200, 300)
        self.assertEqual(alert_type, Alert.Type.GlucoseMild)

    def test_glucose_ranges_hypoglycemia(self):
        alert_type = AlertUtils._glucoseRanges(60, 70, 100, 126, 200, 300)
        self.assertEqual(alert_type, Alert.Type.GlucoseHypoglycemia)

    def test_glucose_ranges_severe(self):
        alert_type = AlertUtils._glucoseRanges(350, 70, 100, 126, 200, 300)
        self.assertEqual(alert_type, Alert.Type.GlucoseSevere)

if __name__ == '__main__':
    unittest.main()