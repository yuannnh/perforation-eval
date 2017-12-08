'''
Some userful functions to make the process automatic
Please modify the following global variables  
'''

from __future__ import division
import subprocess
import os
import numpy as np
from compile import compile as cp
from run_tests import testsForAll as runtests
from compare import ifMutKilled as ifmk

np.set_printoptions(threshold=np.nan)

OUTPUT_ROOT_MUT = '/home/yuan/Desktop/space/outputs_m'
OUTPUT_ROOT_PMUT = '/home/yuan/Desktop/space/outputs_ppm'
# OFFSET is number of caracters before a pmut output folder name,index caracters
# are not counted
OFFSET = 41 
#MUT_MAX = 117111
NUM_MUT_SAMPLE = 1000
NUM_TESTS = 13525


# ____compile and run tests for muts and pmuts in the list____#
def runAllTest(indexes):
	for i in indexes:
		cp("MUT",i,i)
		cp("PMUT",i,i)
		runtests("MUT",i,i)
		runtests("PMUT",i,i)



#____read a pair of mut and pmut tests ouputs,return two array with 
#____length of the NUM_TESTS, 1 means output diff from original one
#____(mut killed), 0 means not killed
def fillRow(m,pm,n):
	for i  in range(NUM_TESTS):
		if ifmk('NAN','MUT',n,i+1):
			m[i] = 1
		if ifmk('PERF','PMUT',n,i+1):
			pm[i] = 1
	return m, pm




#___return mut and pmut n are killed by how many test cases
def checkMut(n):
	m, pm  = np.zeros(13525), np.zeros(13525)
	m, pm  = fillRow(m,pm,n)
	return m.sum(),pm.sum()




#___return a 2 * NUM_MUT_SAMPLE matrix 
#___two row represent mut and pmut
#___each colomn represents a specific mutation
#___a values in the matrix means this mut/pmut is killed by that amount 
#___of tests
def fillResult():
	i = 0
	result = []
	N = NUM_MUT_SAMPLE
	for d,subd,f in os.walk(OUTPUT_ROOT_PMUT):
		if i < N and len(d) > OFFSET:
			#print(d)
			
			n = d[OFFSET:]
			n = int(n)
			result.append(list(checkMut(n)))
			i+=1
			
	return np.array(result)	


