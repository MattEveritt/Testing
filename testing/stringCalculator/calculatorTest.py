import unittest
import calculator

class MyTest(unittest.TestCase):

    def test_SendEmptyString(self):
        ##Arrange
        stringNumbers = "1"
        ##Act
        receive = calculator.Add(stringNumbers)
        ##Assert
        self.assertEqual(receive, sum_digit)

if __name__ == '__main__':
    unittest.main()
