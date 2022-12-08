import unittest
import pandas as pd
from helpers import find_value


class TestFindValue(unittest.TestCase):
    """Test for find_value helper function."""

    def test_correct_input_CT(self):
        df = pd.DataFrame([
            {'sample': 'SCR2-1', 'target': 'TNC2', 'CT': 29.33687528},
            {'sample': 'TNC-1', 'target': 'ACTB', 'CT': 22.923}
            ])
        result = find_value(df, 'SCR2-1', 'TNC2', 'CT')
        self.assertEqual(result, 29.337)
        

    def test_correct_input_dCT(self):
        df = pd.DataFrame([
            {'sample': 'SCR2-1', 'target': 'TNC2', 'dCT': 6.404},
            {'sample': 'TNC-1', 'target': 'TNC2', 'dCT': 6.690}
            ])
        result = find_value(df, 'SCR2-1', 'TNC2', 'dCT')
        self.assertEqual(result, 6.404)
