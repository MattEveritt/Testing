import unittest
import triangle

class MyTest(unittest.TestCase):

    def test_CheckIfAllSidesAreEqualAndReturnEquilateral(self):
        ##Arrange
        a = int(5)
        b = int(5)
        c = int(3)
        
        ##Act
        receive = triangle.checkTriangle(a,b,c)
        
        ##Assert
        self.assertEqual('equilateral', receive)

    def test_CheckIfOnlyTwoSidesAreEqualAndReturnIsosceles(self):
        ##Arrange
        a = int(3)
        b = int(5)
        c = int(4)
        
        ##Act
        receive = triangle.checkTriangle(a,b,c)
        
        ##Assert
        self.assertEqual('isosceles', receive)

    def test_CheckIfNoSidesAreEqualAndReturnIrregular(self):
        ##Arrange
        a = int(3)
        b = int(5)
        c = int(5)
        
        ##Act
        receive = triangle.checkTriangle(a,b,c)
        
        ##Assert
        self.assertEqual('irregular', receive)

if __name__ == '__main__':
    unittest.main()
