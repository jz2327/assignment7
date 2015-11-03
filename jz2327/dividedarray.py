import numpy as np 

'''Problem 2'''

def array_divide():
	'''
	function to solve problem 2: 
	each columns of one array is divided element-wise by another array.
	'''
	array = np.arange(25).reshape(5,5)
	array_divided = np.array([1., 5, 10, 15, 20])
	return np.divide(array.T, array_divided).T