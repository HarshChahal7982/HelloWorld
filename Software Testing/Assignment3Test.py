import unittest
import Assignment3engine

class Mytest(unittest.TestCase):

    def test_send_p_and_r_To_gameWin_Returns_youlose(self):
         #arrange
         comp='p'
         you='r'

         expectedResult=False
         #act
         result=Assignment3engine.gameWin(comp,you)
         # assert
         self.assertEqual(result,expectedResult)

    def test_send_r_and_s_To_gameWin_Returns_youlose(self):
         #arrange
         comp='r'
         you='s'

         expectedResult=False
         #act
         result=Assignment3engine.gameWin(comp,you)
         # assert
         self.assertEqual(result,expectedResult)

    def test_send_p_and_s_To_gameWin_Returns_youwin(self):
         #arrange
         comp='p'
         you='s'

         expectedResult=True
         #act
         result=Assignment3engine.gameWin(comp,you)
         # assert
         self.assertEqual(result,expectedResult)     



if __name__ == '__main__':
    unittest.main()