#!/usr/bin/python3
import subprocess
import shlex
import sys

def run_command(command):
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	while True:
		stdout = process.stdout.readline().decode()[:-1]
#		sys.stdout.write("\r{}".format(stdout))
		print(stdout,end='\r')
		sys.stdout.flush()
		rc = process.poll()
		if rc is not None:
			print()
			break
	return rc

#cmd = shlex.split(input())
cmd = sys.argv[1:]
run_command(cmd)



#popen https://docs.python.org/2/library/subprocess.html
#	stdout, stderr = process.communicate()
