import unittest
from webapp.plugins.validation_utils import isNumberValid, isNameValid

class TestValidationUtils(unittest.TestCase):
    def test_number_valid_false(self):
        number = None
        self.assertFalse(isNumberValid(number))

    def test_number_valid_true(self):
        number = 20
        self.assertTrue(isNumberValid(number))

    def test_name_valid_false(self):
        name = None
        self.assertFalse(isNameValid(name))

    def test_name_valid_true(self):
        name = 'Testing'
        self.assertTrue(isNameValid(name))
