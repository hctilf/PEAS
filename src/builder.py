#lib is path to testing library sources
#file is path to generated test*.cpp
#nanobench is path to nanobench header, most likely is '.'
#look at the previos commits for debugging module

import os
import subprocess
import sys

COMP = 'g++'
OPTIMISATION = ['-O0', '-O1', '-O2', '-O3', '-Ofast']

def find_files():
	files = [entry.name for entry in os.scandir(os.getcwd()) if entry.name.startswith('test') and entry.name.endswith('.cpp') and entry.is_file() and not entry.name == 'nanobench.h']
	for f in files: print(f)
	return files


def build(lib, file, nanobench = '.'):
	for file in find_files():
		for oX in OPTIMISATION:
			subprocess.run([COMP, '-I'+nanobench, lib, file,\
				oX, '-o', file[:len(file)-4]+oX[1:]])

#build(sys.argv[1], sys.argv[2])