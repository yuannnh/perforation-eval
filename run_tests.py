#######################################################################
# testForAll function can execute a serie of testcases by specifying #
# the mode and the start and end index of mutant, tests are executed #
# the pair (mut and pmut)                                            #
# please modify the following paths                                  #
# if you are using this script for other programs, you should also   #
# modify the makeCmd function, because the test exectution command   #
# can be different                                                   #
#######################################################################
import subprocess
import os

BASE_DIR = "/home/yuan/Desktop/space/"
MUT_SRC = BASE_DIR + "mutants/"
MUT_BIN = MUT_SRC + "bin/"
#PMUT_SRC = BASE_DIR + "p_mutants/"
PMUT_SRC = BASE_DIR + "pp_mutants/"
PMUT_BIN = PMUT_SRC + "bin/"
MUT_PREFIX = "space.MUT"
#PMUT_PREFIX = "space_p.MUT"
PMUT_PREFIX = "space_pp.MUT"
MUT_OUTPUT_PREFIX = BASE_DIR + "outputs_m/MUT"
#PMUT_OUTPUT_PREFIX = BASE_DIR + "outputs_pm/PMUT"
PMUT_OUTPUT_PREFIX = BASE_DIR + "outputs_ppm/PMUT"
RUN_TEST_SCRIPT_DIR = BASE_DIR + "scripts/run_test/"
TEST_MAX = 13525

# make the command to execute on test
# exec_indice: the executable to run 
def makeCmd(mode,exec_indice,t_indice):
	if mode == "MUT":
		cmd1 = MUT_BIN + MUT_PREFIX + exec_indice + " ../inputs/gr" + t_indice + " > " + MUT_OUTPUT_PREFIX  + exec_indice +"/output_gr" + t_indice + "_m.txt"
		cmd2 = "echo $? > " + MUT_OUTPUT_PREFIX + exec_indice + "/exit_gr" + t_indice + "_m.txt"

	elif mode == "PMUT":
		cmd1 = PMUT_BIN + PMUT_PREFIX + exec_indice + " ../inputs/gr" + t_indice + " > " + PMUT_OUTPUT_PREFIX + exec_indice +"/output_gr" + t_indice + "_m.txt"
		cmd2 = "echo $? > " + PMUT_OUTPUT_PREFIX + exec_indice + "/exit_gr" + t_indice + "_m.txt"
	print (cmd1)	
	return [cmd1,cmd2]

#execute all tests for one executable
def testsForOneExec(mode,exec_indice):
	if mode == "MUT":
		out_prefix = MUT_OUTPUT_PREFIX 
	elif mode == "PMUT":
		out_prefix = PMUT_OUTPUT_PREFIX 
	if os.path.exists(out_prefix + str(exec_indice)) == False:
			creat_dir = "mkdir " + out_prefix + str(exec_indice)
			process = subprocess.Popen(creat_dir.split(), stdout=subprocess.PIPE)
			output, error = process.communicate()
	script = RUN_TEST_SCRIPT_DIR  + mode + str(exec_indice) + ".sh"
	if os.path.exists(script) == False:
			creat_file = "touch " + script
			mk_exec = "chmod 777 " +script
			process = subprocess.Popen(creat_file, shell = True, stdout=subprocess.PIPE)
			output, error = process.communicate()
			process = subprocess.Popen(mk_exec.split(), stdout=subprocess.PIPE)
			output, error = process.communicate()
	
	with open(script, 'w') as f:
		f.write("#!/bin/bash\n")
		for i in range(1, TEST_MAX+1):
			cmd1, cmd2  = makeCmd(mode, str(exec_indice), str(i))
			f.write(cmd1 + "\n")
			f.write(cmd2 + "\n")
	process = subprocess.Popen(script.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	'''
	for i in range(1, TEST_MAX+1):
		cmd1, cmd2  = makeCmd(mode, str(exec_indice), str(i))
		cmd0 = "echo $HOME"
		process = subprocess.Popen(cmd1.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		process = subprocess.Popen(cmd2.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
	'''
		
# execute tests for executables from start indice to end indice	
def testsForAll(mode,start,end):
	for i in range(start, end+1):
		testsForOneExec(mode,i)



