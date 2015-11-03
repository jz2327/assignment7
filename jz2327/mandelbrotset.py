import numpy as np 
import math
import matplotlib.pyplot as plt 

'''Problem 4: A class is created to generate a mandelbrot set by the required interation.'''

class mandelbrot():
	'''
	The mandelbrot class would take two arrays' arguments as the grid of the new mandelbrot set.
	It contains functions including do the interation and create the mandelbrot set.
	'''

	def __init__(self, array1, array2):
		self.N_max = 50
		self.some_threshold = 50
		self.x_coordinate = array1
		self.y_coordinate = array2
		self.metrics_origin = np.zeros([len(array1),len(array2)], complex)
		self.metrics_interation = np.zeros([len(array1),len(array2)], complex)

	def mandelbrot_set(self):
		'''Generate the origin mandelbrot set.'''

		for i in range(len(self.x_coordinate)):
			for k in range(len(self.y_coordinate)):
				c = self.x_coordinate[i] + 1j * self.y_coordinate[k]
				self.metrics_origin[i,k] = c
		return self.metrics_origin


	def mandelbrot_interation(self):
		'''Genrate the mandelbrot set by interation.'''

		self.metrics_interation = self.mandelbrot_set()
		self.metrics_set = self.metrics_interation.copy()
		for v in range(self.N_max):
			for i in range(len(self.x_coordinate)):
				for j in range(len(self.y_coordinate)):
					if abs(self.metrics_interation[i][j]) < self.some_threshold:
						self.metrics_interation[i][j] = self.metrics_interation[i][j]**2 + self.metrics_set[i][j]
					else:
						pass
		return self.metrics_interation
    
	def is_mandelbrot_set(self):
		'''Generate the valid mandelbrot set of boolean value True and False meeting the requirement'''

		return abs(self.mandelbrot_interation()) < self.some_threshold


#	def __repr__(self):
#		return self.mandelbrot_set()

