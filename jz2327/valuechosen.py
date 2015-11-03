import numpy as np

'''Problem 3'''

def value_choose():
	'''Choose values according to given requirement from a given array by fancy indexing.'''
	
	array = np.random.rand(10,3)
	array_sort = np.argsort(abs(array-0.5))
	fancy_order = array_sort[:, 0]
	return array[np.arange(0,10), fancy_order]
