import numpy as np 

'''Problem 1'''

def array_generate():
	'''Generate a new array as required.'''
	return np.arange(1,16,1).reshape(3,5).T

def array_rows_on(array):
	'''Generate a new array containing 2nd and 4th rows.'''
	array = array_generate()
	return np.array([array[1], array[3]])

def array_columns_on(array):
	'''Generate a new array containing 2nd column.'''
	array = array_generate()
	return array[:, 1:2]

def array_rectangular(array):
	'''Generate a new array between coordinates [1,0] and [3,2]'''
	array = array_generate()
	return array[1:4, :]

def array_values(array):
	'''Generate a new array with value between 3 and 11'''
	array = array_generate()
	array_larger_3 = array[array >= 3]
	array_between_3_11 = array_larger_3[array_larger_3 <= 11]
	return array_between_3_11