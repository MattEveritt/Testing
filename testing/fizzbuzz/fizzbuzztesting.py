import unittest
import fizzbuzz

class MyTest(unittest.TestCase):

    def test_Send_1_ToFizzBuzzerAndItReturns_1(self):
        ##Arrange
        value = 1
        ##Act
        receive = fizzbuzz.FizzBuzzer(value)
        ##Assert
        self.assertEqual(receive, value)

    def test_Send_2_ToFizzBuzzerAndItReturns_2(self):
        ##Arrange
        value = 2
        ##Act
        receive = fizzbuzz.FizzBuzzer(value)
        ##Assert
        self.assertEqual(receive, value)

    def test_Send_3_ToFizzBuzzerAndItReturns_Fizz(self):
        ##Arrange
        value = 3
        expect = "Fizz"
        ##Act
        receive = fizzbuzz.FizzBuzzer(value)
        ##Assert
        self.assertEqual(receive, expect)

    def test_Send_4_ToFizzBuzzerAndItReturns_4(self):
        ##Arrange
        value = 4
        ##Act
        receive = fizzbuzz.FizzBuzzer(value)
        ##Assert
        self.assertEqual(receive, value)

    def test_Send_5_ToFizzBuzzerAndItReturns_Buzz(self):
        ##Arrange
        value = 5
        expect = "Buzz"
        ##Act
        receive = fizzbuzz.FizzBuzzer(value)
        ##Assert
        self.assertEqual(receive, expect)

    def test_Send_6_ToFizzBuzzerAndItReturns_Fizz(self):
        ##Arrange
        value = 6
        expect = "Fizz"
        ##Act
        receive = fizzbuzz.FizzBuzzer(value)
        ##Assert
        self.assertEqual(receive, expect)

    def test_Send_7_ToFizzBuzzerAndItReturns_7(self):
        ##Arrange
        value = 7
        ##Act
        receive = fizzbuzz.FizzBuzzer(value)
        ##Assert
        self.assertEqual(receive, value)

    def test_Send_15_ToFizzBuzzerAndItReturns_FizzBuzz(self):
        ##Arrange
        value = 15
        expect = "FizzBuzz"
        ##Act
        receive = fizzbuzz.FizzBuzzer(value)
        ##Assert
        self.assertEqual(receive, expect)

if __name__ == '__main__':
    unittest.main()
