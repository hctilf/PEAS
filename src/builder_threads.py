#lib is path to testing library sources
#file is path to generated test*.cpp
#nanobench is path to nanobench header, most likely is '.'
#look at the previos commits for debugging module

import os
import subprocess
import sys
import threading

COMP = 'g++'
OPTIMISATION = ['-O0', '-O1', '-O2', '-O3', '-Ofast']
THREADS = []

lib = sys.argv[1]


class buildThread(threading.Thread):
	def __init__(self, id, task) -> None:
		self.id = id
		self.file = task
		threading.Thread.__init__(self)

	def run(self):
		global lib
		for oX in OPTIMISATION:
			subprocess.run([COMP, '-I.', lib, self.file,\
				oX, '-o', self.file[:len(self.file)-4]+oX[1:]])

def find_files():
	files = [entry.name for entry in os.scandir(os.getcwd()) if entry.name.startswith('test') and entry.name.endswith('.cpp') and entry.is_file() and not entry.name == 'nanobench.h']
	for f in files: print(f)
	return files


def build(lib, file, nanobench = '.'):
	for id, file in enumerate(find_files()):
		thread = buildThread(id, file)
		thread.start()
		THREADS.append(thread)

build(sys.argv[1], sys.argv[2])

for thread in THREADS:
    thread.join()