import unittest
import calculator

class MyTest(unittest.TestCase):

    def test_CalculateSumOfIntegers_A_And_b_And_AssignCalculatedSumToIntegerC(self):
        ##Arrange
        a = int(3)
        b = int(5)
        
        ##Act
        receive = calculator.addition(a,b)
        
        ##Assert
        self.assertEqual(8, receive)

if __name__ == '__main__':
    unittest.main()
