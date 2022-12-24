#lib is path to testing library sources
#file is path to generated test*.cpp
#nanobench is path to nanobench header, most likely is '.'
#look at the previos commits for debugging module

import os
import subprocess
import sys
import threading
import time

COMP = 'g++'
OPTIMISATION = ['-O0', '-O1', '-O2', '-O3', '-Ofast']

buildMutex = threading.Lock()
cpuCnt = os.cpu_count()
<<<<<<< HEAD
nanobench = parDir = f'/home/{os.getlogin()}/PEAS'
curDir = parDir + '/src'

threadC = []
lib, hfile, nanobench = sys.argv[1], sys.argv[2], sys.argv[3]
=======
curDir = os.getcwd()
parDir = os.path.split(curDir)[0]
lib = sys.argv[1]
threadC = []
>>>>>>> 8b13cd66491c8b837c78a6913b098c335fffafd9

def time_prog(func):	#time measurement
	def wrapper(*args):
		start = time.time()
		func(*args)
		print(time.time() - start)
	return wrapper

class buildThreadMain(threading.Thread):
<<<<<<< HEAD
	def __init__(self, id, mutex, task) -> None:
=======
	def __init__(self, id, mutex,task) -> None:
>>>>>>> 8b13cd66491c8b837c78a6913b098c335fffafd9
		self.id = id
		self.mutex = mutex
		self.file = task
		threading.Thread.__init__(self)

	def run(self):
		if cpuCnt <= 4:
			with self.mutex:
				for id, oX in enumerate(OPTIMISATION):
					threadC.append([])
					thread = buildThreadChild(id, oX, buildMutex, self.file)
					thread.start()
					threadC[id].append(thread)
		else:
			for id, oX in enumerate(OPTIMISATION):
				threadC.append([])
				thread = buildThreadChild(id, oX, buildMutex, self.file)
				thread.start()
				threadC[id].append(thread)

class buildThreadChild(threading.Thread):
	def __init__(self, id, oX, mutex, task) -> None:
		self.id = id
		self.oX = oX
		self.mutex = mutex
		self.file = task
		threading.Thread.__init__(self)

	def run(self):
		global lib
		if cpuCnt <= 2:
			with self.mutex:
<<<<<<< HEAD
				subprocess.run([COMP, '-I'+nanobench, '-I'+hfile, lib, f'{parDir}/{self.file}',\
					self.oX, '-o', f"{parDir}/tmp/{self.file[:-4]}/{self.file[:len(self.file)-4]}{self.oX[1:]}"])
		else:
			subprocess.run([COMP, '-I'+nanobench, '-I'+hfile, lib, f'{parDir}/{self.file}',\
				self.oX, '-o', f"{parDir}/tmp/{self.file[:-4]}/{self.file[:len(self.file)-4]}{self.oX[1:]}"])	

def find_files():
	files = [entry.name for entry in os.scandir(parDir) if entry.name.startswith('test') and entry.name.endswith('.cpp') and entry.is_file() and not entry.name == 'nanobench.h']
	return files

@time_prog
def build(lib, hfile):
	if not os.path.exists(f"{parDir}/tmp"):
		os.mkdir(f"{parDir}/tmp")

	for id, file in enumerate(find_files()):
		print(id, file)
=======
				subprocess.run([COMP, '-I.', lib, self.file,\
					self.oX, '-o', f"{parDir}/tmp/{self.file[:-4]}/{self.file[:len(self.file)-4]}{self.oX[1:]}"])
		else:
			subprocess.run([COMP, '-I.', lib, self.file,\
				self.oX, '-o', f"{parDir}/tmp/{self.file[:-4]}/{self.file[:len(self.file)-4]}{self.oX[1:]}"])	

def find_files():
	files = [entry.name for entry in os.scandir(os.getcwd()) if entry.name.startswith('test') and entry.name.endswith('.cpp') and entry.is_file() and not entry.name == 'nanobench.h']
	for f in files: print(f)
	return files

@time_prog
def build(lib, file, nanobench = '.'):
	if not os.path.exists(f"{parDir}/tmp"):
		os.mkdir(f"{parDir}/tmp")
	for id, file in enumerate(find_files()):
>>>>>>> 8b13cd66491c8b837c78a6913b098c335fffafd9
		if not os.path.exists(f"{parDir}/tmp/{file[:-4]}"):
			os.mkdir(f"{parDir}/tmp/{file[:-4]}")
		thread = buildThreadMain(id, buildMutex, file)
		thread.start()
	for threadList in threadC:
		for thread in threadList: thread.join()

<<<<<<< HEAD
build(lib, hfile)
=======
build(sys.argv[1], sys.argv[2])
>>>>>>> 8b13cd66491c8b837c78a6913b098c335fffafd9
