import unittest
import age

class ageUnitTests(unittest.TestCase):

    def test_CheckIfUserIsUnder_18_AndIfCorrectReturnYouAreAChild(self):
        ##Arrange
        a = int(20)

        ##Act
        receive = age.ages(a)

        ##Assert
        self.assertEqual("You are a child", receive)

    def test_CheckIfUserIsUnder_70_AndIfCorrectReturnYouAreAnAdult(self):
        ##Arrange
        a = int(80)

        ##Act
        receive = age.ages(a)

        ##Assert
        self.assertEqual("You are an adult", receive)

    def test_CheckIfUserIsAbove_70_AndIfCorrectReturnYouAreAPensioner(self):
        ##Arrange
        a = int(60)

        ##Act
        receive = age.ages(a)

        ##Assert
        self.assertEqual("You are a pensioner", receive)

if __name__ == '__main__':
    unittest.main()
