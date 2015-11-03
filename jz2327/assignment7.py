import numpy as np
import matplotlib.pyplot as plt 
import generatearray
import dividedarray
import valuechosen
import mandelbrotset
from mandelbrotset import mandelbrot

'''
Main program for assignment 7. 
Use difined modules to generate answers for each question.
'''

try:
	#problem 1
	print 'Problem 1:'
	print 'Generate a new array as required:'
	array_new = generatearray.array_generate()
	print array_new

	print 'Generate a new array containing the 2nd and 4th rows:'
	print generatearray.array_rows_on(array_new)

	print 'Generate a new array that contains the 2nd column:'
	print generatearray.array_columns_on(array_new)

	print 'Generate a new array that contains all the elements in the rectangular section between the coordinates'
	print  generatearray.array_rectangular(array_new)

	print 'Generate a new array that contains only elements with values that are between 3 and 11:'
	print generatearray.array_values(array_new)

	#problem 2
	print 'Problem 2:'
	print dividedarray.array_divide()

	#problem 3
	print 'Problem 3:'
	print valuechosen.value_choose()

	#problem 4
	print 'problem 4:'
	array1 = np.arange(-2, 1, 0.01)
	array2 = np.arange(-1.5, 1.5, 0.01)
	mandelbrot_set_generate = mandelbrot(array1, array2)
	mask = mandelbrot_set_generate.is_mandelbrot_set()
	#plot the graph and save it to 'mandelbrot.png'
	plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig('mandelbrot.png')

except KeyboardInterrupt:
	print '\n Error: Interrupted by user'
except ArithmeticError:
	print '\n Mathematic Error: Arithmetic'
except OverflowError:
	print '\n Mathematic Error: Overflow'
except ZeroDivisionError:
	print '\n Mathematic Error: Divided by Zero'
except ValueError:
	print '\n Value Error: Invalid Value'
except TypeError:
	print '\n Type Error: Invalid Type'


