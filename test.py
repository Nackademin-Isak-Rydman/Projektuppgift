import unittest
import klient

class TestCases(unittest.TestCase):

    def test_check_message(self):
        expected_result1 = True
        expected_result2 = False

        string = ""
        string2 = "hej"
        actual_result = klient.check_message(string)
        actual_result2 = klient.check_message(string2)

        self.assertEqual(expected_result2, actual_result)
        self.assertEqual(expected_result1, actual_result2)

if __name__ == '__main__':
    unittest.main()