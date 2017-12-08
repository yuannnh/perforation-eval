'''
ifmk function is to compare the output difference between the non-
mutated one and the mutated one for a single testcase, you should 
specify the two modes to be compared(NAN with MUT or PERF with PMUT,
mutated mode should be the mode2), the index of mutant and the index of 
the test case
'''


from __future__ import division
from difflib import Differ
from analyse import countCrashMut as countCrashMut
import sys

PATH_PREFIX = "/home/yuan/Desktop/space/"
NAN = ""
MUT = "_m"
#PERF = "_p"
PERF = "_pp"
#PMUT = "_pm"
PMUT = "_ppm"
NUM_TESTS = 13525

def compare(F1,F2):
	diffs = []
	try:
		with open(F1) as f1, open(F2) as f2:
			differ = Differ()
			#diffs = list(differ.compare(f1.readlines(), f2.readlines()))
			for line1, line2 in zip(f1,f2):
				if line1.encode('utf-8') != line2.encode('utf-8'):
					diffs.append(line1+line2)
	except UnicodeDecodeError:
		#e = sys.exc_info()[1]
		#print(e.args[0]) 
		#print(F1)
		#print(F2)
		diffs.append('utf-8 error cause diff')
	return diffs

			
def makePath(x,mode1,mode2,m_index):
	if mode1 == "NAN":
		suffix1 = NAN
		suffix11 = ""
	elif mode1 == "PERF":
		suffix1 = PERF
		suffix11 = PERF
	if mode2 == "MUT":
		suffix2 = MUT + "/MUT" + str(m_index)
		suffix21 = MUT
	elif mode2 == "PMUT":
		suffix2 = PMUT + "/PMUT" + str(m_index)
		suffix21 = MUT
	elif mode2 == "PERF":
		suffix2 = PERF
		suffix21 = PERF

	p1 = PATH_PREFIX + "outputs" + suffix1 + "/output_gr"+str(x) + suffix11 + ".txt"
	p2 = PATH_PREFIX + "outputs" + suffix2 + "/output_gr"+str(x) + suffix21 + ".txt"	
	return p1, p2

		
def compareAll(mode1,mode2,mut_index = 0):	
	counter = 0
	for i in range(1,NUM_TESTS+1):

		p1, p2 = makePath(i,mode1,mode2,mut_index)
		#p1, p2 = makeMutPmutPath(i,mut_index)
		result = compare(p1,p2)
		if result:
			counter+=1
			#print("**" + str(i))
			#for i in range(len(result)):
				#print("**"+str(i)+"**")
				#print(result[i])
	#print("********************************************************")
	#print("********************************************************")		
	#print("DIFF RESULT FILES: " + str(counter))
	#print("DIFF RATE: " + str(counter/NUM_TESTS))
	return counter
	
#____return if the mut is killed by a one test 	
def ifMutKilled(mode1, mode2, mut_idx, test_idx):
	p1, p2 =  makePath(test_idx,mode1,mode2,mut_idx)
	res = compare(p1,p2)
	if not res:
		return False
	else:
		return True
	
def ifCrash(path):
	with open(path) as f:
		for line in f:
			if line[0] != "0":
				return True
			else:
				return False
				
	
def countCrash(mode):
	counter = 0
	for i in range(1,NUM_TESTS+1):
		path = PATH_PREFIX + "outputs" + mode + "/exit_gr"+str(i) + mode + ".txt"
		if ifCrash(path):
			counter+=1
			#print(str(i))
	return counter

