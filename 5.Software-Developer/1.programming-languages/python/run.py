#!/usr/bin/python3
import subprocess, sys
process = subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE)
while process.poll() is None:
  stdout = process.stdout.readline().decode()[:-1]
  print(stdout,end='\r')
print()
