#Name: Tarini Srikanth
#Instructor: Turner-05
#Project: Lab 2
import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here. REMOVE PASS
      self.assertEqual(funcs.f(5),185)
      
   def test_f_2(self):
      # Add code here. REMOVE PASS
      self.assertEqual(funcs.f(0),0)
   
   def test_f_3(self):
      self.assertEqual(funcs.f(1),9)

   def test_g_1(self):
      # Add code here. REMOVE PASS
      self.assertRaises(ZeroDivisionError, funcs.g,0,3)
   
   def test_g_2(self):
      self.assertEqual(funcs.g(3,0),1)
   
   def test_g_3(self):
      self.assertAlmostEqual(funcs.g(2,7),8.833333333)
   
   def test_hypotenuse(self):
      self.assertEqual(funcs.hypotenuse(3,4),5)
   
   def test_hypotenuse(self):
      self.assertEqual(funcs.hypotenuse(1,0),1)
   
   def is_positive_test(self):
      self.assertEqual(funcs.is_positive(4),True)
   
   def is_positive_test(self):
      self.assertEqual(funcs.is_positive(-2),False)

   
   
   # Add five more tests...

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

