import string
import unittest
import Assignment1engine

class Mytest(unittest.TestCase):
     
    #  1. Test Case for age under 18
      def test_send_17_To_agecalculation_Returns_youareachild(self):
       
        #Arrange
        age=int(17)
        expectedResult="You are a child" 
        #act
        result=Assignment1engine.agecalculation(age)
        # assert
        self.assertEqual(result,expectedResult)


    #  Test case for age greater than 18 and under 70
      def test_send_38_To_agecalculation_Returns_youareanadult(self):
       
        #Arrange
        age=int(38)
        expectedResult="You are an adult"
        #act
        result=Assignment1engine.agecalculation(age)
        # assert
        self.assertEqual(result,expectedResult)

  #  Test case for age greater than 70
      def test_send_84_To_agecalculation_Returns_youareapensioner(self):
       
        #Arrange
        age=int(84) 
        expectedResult="You are a pensioner"
        #act
        result=Assignment1engine.agecalculation(age)
        # assert
        self.assertEqual(result,expectedResult)



if __name__ == '__main__':
    unittest.main()


   

