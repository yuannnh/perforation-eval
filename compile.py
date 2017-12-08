####################################################################
# The compile function can be called to comile a serie of files by #
# specifying the mode start index and end index                    #
# modifiy the followin variables for mut and pmut path             #
####################################################################
import subprocess
BASE_DIR = "../"
MUT_SRC = BASE_DIR + "mutants/"
MUT_BIN = MUT_SRC + "bin/"
#PMUT_SRC = BASE_DIR + "p_mutants/"
PMUT_SRC = BASE_DIR + "pp_mutants/"
PMUT_BIN = PMUT_SRC + "bin/"
MUT_PREFIX = "space.MUT"
#PMUT_PREFIX = "space_p.MUT"
PMUT_PREFIX = "space_pp.MUT"



# mode should be MUT or PMUT
def makeCompileCmd(mode,n):
	if mode == "MUT":
		cmd1 = "gcc " + MUT_SRC + MUT_PREFIX + str(n) + ".c -lm -o " + MUT_BIN + MUT_PREFIX + str(n)
		#cmd2 = "mv " + MUT_PREFIX + str(n) + " ./bin"
	elif mode == "PMUT":
		cmd1 = "gcc " + PMUT_SRC + PMUT_PREFIX + str(n) + ".c -lm -o " + PMUT_BIN + PMUT_PREFIX + str(n)
		#cmd2 = "mv " + PMUT_PREFIX + str(n) + " ./bin"
	return cmd1	
def compile(mode, start, end):
		
	for i in range(start, end+1):
		#cmd1,cmd2 =  makeCompileCmd(mode, i)
		cmd1 = makeCompileCmd(mode, i)
		process = subprocess.Popen(cmd1.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		if error:
			print(mode + str(i) + error)
		'''
		process = subprocess.Popen(cmd2.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		if error:
			print(mode + str(i) + error)
		'''

		
	
