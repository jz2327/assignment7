import numpy as np 
import unittest
from unittest import TestCase
import mandelbrotset
from mandelbrotset import mandelbrot 

'''test the mandelbrot class.'''

class assignment7_test(TestCase):

	def test_class_init(self):
		'''test the class argument of two arrays is valid.'''

		a = np.arange(0, 10)
		b = np.arange(0, 5)
		mandelbrot_init = mandelbrot(a, b)

		self.assertTrue(np.array_equal(mandelbrot_init.x_coordinate, a))
		self.assertTrue(np.array_equal(mandelbrot_init.y_coordinate, b))

	def test_class_mandelbrot_set(self):
		'''test the mandelbrot_set function generates the right return.'''

		a = np.arange(1,3)
		b = np.array([[1+1j*1, 1+1j*2],[2+1j*1, 2+1j*2]])
		mandelbrot_init = mandelbrot(a, a)
		mandelbrot_set_1 = mandelbrot_init.mandelbrot_set()
		self.assertTrue(np.array_equal(mandelbrot_set_1, b))

	def test_class_mandelbrot_interation(self):
		'''test the mandelbrot_interation function generates the right return.'''

		a = np.arange(1,3)
		b = np.array([[1.-97.j,478.+1366.j],[2.+51.j,-94.+42.j]])
		mandelbrot_init = mandelbrot(a, a)
		mandelbrot_interation_1 = mandelbrot_init.mandelbrot_interation()
		self.assertTrue(np.array_equal(mandelbrot_interation_1, b))

	def test_class_is_mandelbrot_set(self):
		'''test the is_mandelbrot_set function generates the right return.'''

		a = np.arange(1,3)
		b = np.array([[False, False], [False, False]], dtype=bool)
		mandelbrot_init = mandelbrot(a, a)
		mandelbrot_is_set = mandelbrot_init.is_mandelbrot_set()
		self.assertTrue(np.array_equal(mandelbrot_is_set, b))

if __name__ == '__main__':
	unittest.main()