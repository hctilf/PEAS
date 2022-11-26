#lib is path to testing library sources
#file is path to generated test*.cpp
#nanobench is path to nanobench header, most likely is '.'
#look at the previos commits for debugging module

import os
import subprocess
import sys
from multiprocessing import Process

COMP = 'g++'
OPTIMISATION = ['-O0', '-O1', '-O2', '-O3', '-Ofast']
PROCS = []

def builderProc(lib, file):
    for oX in OPTIMISATION:
        p = Process(target=buildProcOne, args=[oX, lib, file])
        p.start()
        PROCS.append(p)

def buildProcOne(oX, lib, file):
    subprocess.run([COMP, '-I.', lib, file, oX, '-o', file[:len(file)-4]+oX[1:]])    

def find_files():
	files = [entry.name for entry in os.scandir(os.getcwd()) if entry.name.startswith('test') and entry.name.endswith('.cpp') and entry.is_file() and not entry.name == 'nanobench.h']
	for f in files: print(f)
	return files


def build(lib, file, nanobench = '.'):
    for file in find_files():
        p = Process(target=builderProc, args=[lib, file])
        p.start()
        PROCS.append(p)

build(sys.argv[1], sys.argv[2])

for p in PROCS: p.join()