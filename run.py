'''
a example of using these functions to make the process automatic
but this example might not work because some of the mutants may give 
errors while running, these problems should be handled manually.
there are only headlines of each step, you can find more details in each
functions comments
This script is not tested
'''
from utile import *
import numpy as np

NUM_MUT_SAMPLE = 1000
NUM_TESTS = 13525
MAX_MUT_IDX = 117111

# generate the mut indexes list randomly
mut_to_test = np.random.randint(MAX_MUT_IDX,NUM_MUT_SAMPLE)
mut_to_test+=1

# compile and run tests for these mut and pmut according to the list generated
runAllTest(mut_to_test)

# construct a result matrix
result_matrix = fillResult()

# analyse result matrix
killed_rates = np.count_nonzero(result_matrix,axis = 0) / NUM_MUT_SAMPLE
print("mut killed rate: ", killed_rates[0])
print("pmut killed rate: ", killed_rates[1])

