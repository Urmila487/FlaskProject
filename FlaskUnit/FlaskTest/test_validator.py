import unittest

from Common_Functions import *


class TestValidator(unittest.TestCase):

    def test_response_check_success(self):
        result = responce_check(200)
        print('Status code output is Valid', result)
        self.assertTrue(result)

    def test_response_check_Failure(self):
        result = responce_check(2000)
        print('Status code output is InValid', result)
        self.assertFalse(result)

    def test_response_check_Failure(self):
        result = responce_check(20)
        print('Status code output is InValid', result)
        self.assertFalse(result)

    def test_response_check_Failure(self):
        result = responce_check(500)
        print('Status code output is InValid', result)
        self.assertFalse(result)

    def test_check_status_is_valid(self):
        result = status_check('SUCCESS')
        print('Status Check Success:', result)
        self.assertTrue(result)

    def test_check_status_is_Invalid(self):
        result = status_check('Succes')
        print('Status Check Failure:', result)
        self.assertFalse(result)

    def test_check_status_is_Invalid(self):
        result = status_check('Failure')
        print('Status Check Failure:', result)
        self.assertFalse(result)

    def test_respone_token_is_not_valid(self):
        result = response_token_check('NULL')
        print('Response Token Success:', result)
        self.assertTrue(result)

    def test_check_put_response_status_is_valid(self):
        result = status_check('SUCCESS')
        print('Put responses status Check Success:', result)
        self.assertTrue(result)

    def test_check_put_response_status_is_invalid(self):
        result = status_check('Failure')
        print(' Put responses status Check Failure:', result)
        self.assertFalse(result)

    def test_get_data_is_valid(self):
        Expected_value1 = {"message": "retrieval succesful",
                           "payload": {"firstname": "Urmila", "lastname": "Vadi", "phone": "408329191"},
                           "status": "SUCCESS"}
        Actual_value1 = {"message": "retrieval succesful",
                         "payload": {"firstname": "Urmila", "lastname": "Vadi", "phone": "408329191"},
                         "status": "SUCCESS"}
        result = get_data_is_check(Expected_value1,Actual_value1)
        self.assertEqual(Expected_value1,Actual_value1)
        print('Test data is Valid:', result)


    def test_get_data_is_invalid(self):
        Expected_value1 = {"message": "retrieval succesful",
                           "payload": {"firstname": "Urmila", "lastname": "Vadi", "phone": "408329191"},
                           "status": "Failure"}
        Actual_value1 = {"message": "retrieval succesful",
                         "payload": {"firstname": "Urmila", "lastname": "Vadi", "phone": "408329191"},
                         "status": "SUCCESS"}
        result = get_data_is_check(Expected_value1,Actual_value1)
        self.assertNotEqual(Expected_value1,Actual_value1)
        print('Test data is InValid:', result)


if __name__ == '__main__':
    unittest.main()
