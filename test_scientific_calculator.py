import unittest
import math

from scientific_calculator import cos_method, sin_method, tan_method, sqrt_method, log_method, exp_method


class test_scientific_calculator(unittest.TestCase):
   
# Test cases for sin
   
    def test_sin_positive(self):
        result=sin_method(90)
        self.assertAlmostEqual(result,1)

    def test_sin_negative(self):
        result=sin_method(-90)
        self.assertAlmostEqual(result,-1)

    def test_sin_zero(self):
        result=sin_method(0)
        self.assertAlmostEqual(result,0)


    def test_sin_non_numeric(self):
        with self.assertRaises(TypeError):
            sin_method("hello")
    
#Test cases for cos

    def test_cos_positive(self):
        result=cos_method((90))
        self.assertAlmostEqual(result,0)

    def test_cos_negative(self):
        result=cos_method(-90)
        self.assertAlmostEqual(result,0)

    def test_cos_zero(self):
        result=cos_method(0)
        self.assertAlmostEqual(result,1)


    def test_cos_non_numeric(self):
        with self.assertRaises(TypeError):
            cos_method("hello")

#test cases for tan

    def test_tan_positive(self):
        result=tan_method(45)
        self.assertAlmostEqual(result,1)

    def test_tan_negative(self):
        result=tan_method(-45)
        self.assertAlmostEqual(result,-1)

    def test_tan_zero(self):
        result=tan_method(0)
        self.assertAlmostEqual(result,0)


    def test_tan_non_numeric(self):
        with self.assertRaises(TypeError):
            tan_method("hello")


#test cases for sqrt

    def test_sqrt_Positve(self):
        result=sqrt_method(4)
        self.assertEqual(result,2)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt_method(-4)
            
    def test_sqrt_zero(self):
        result=sqrt_method(0)
        self.assertEqual(result,0)
    
    def test_sqrt_non_numeric(self):
        with self.assertRaises(TypeError):
            sqrt_method("hola")


#test cases for log

    def test_log_positive(self):
        result=log_method(10)
        self.assertAlmostEqual(result,2.302585092994046, places=7)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            log_method(-1)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            log_method(0)
        
    def test_log_non_numeric(self):
        with self.assertRaises(TypeError):
            log_method("hello")


 #test cases for exp

    def test_exp_positive(self):
        result=exp_method(3)
        self.assertEqual(result,20.085536923187668)

    def test_exp_negative(self):
        result=exp_method(-2)
        self.assertEqual(result,0.1353352832366127)
    
    def test_exp_zero(self):
        result=exp_method(0)
        self.assertEqual(result,1)
    
    def test_exp_non_numeric(self):
        with self.assertRaises(TypeError):
            exp_method("hello")





if __name__=='__main__':
    unittest.main()
