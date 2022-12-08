import os, sys, subprocess, psutil, threading
from builder import *
from  generator import *
import builder as bd
#generator needs one additional argument: .h file parent directory
#subprocess.run(['python3', 'generator.py', '/home/majong/PEAS/src/'])

f = open('/sys/devices/system/cpu/cpu0/cache/index3/size', 'r')
l3 = int((f.readline().replace('K', '')))*1024
f.close()
print(l3)
mem_req = generator('/home/vadim/PEAS/src/')

#generator needs one additional argument: first is path to library sources, the second one is parent directory to testSOMETHING.cpp 
#subprocess.run(['python3', 'builder.py', '/home/majong/PEAS/src/lsm.cpp', '/home/majong/PEAS/src/'])
buildMutex = threading.Lock()
cpuCnt = os.cpu_count()
curDir = os.getcwd()
parDir = os.path.split(curDir)[0]
lib = sys.argv[1]
threadC = []


class buildThreadMain(threading.Thread):
	def __init__(self, id, mutex, task) -> None:
		self.id = id
		self.mutex = mutex
		self.file = task
		threading.Thread.__init__(self)

	def run(self):
		if cpuCnt <= 4:
			with self.mutex:
				for id, oX in enumerate(mem_req):
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
				subprocess.run([COMP, '-I.', lib, self.file,\
					self.oX, '-o', f"{parDir}/tmp/{self.file[:-4]}/{self.file[:len(self.file)-4]}{self.oX[1:]}"])
		else:
			subprocess.run([COMP, '-I.', lib, self.file,\
				self.oX, '-o', f"{parDir}/tmp/{self.file[:-4]}/{self.file[:len(self.file)-4]}{self.oX[1:]}"])	


class execute():
	def __init__(self) -> None:
		self.mem_req = []
		self.testing = [i[0] for i in mem_req]
		self.mainDir = os.path.split(os.getcwd())[0]
		self.tmpDir = self.mainDir + '/tmp'
		self.dirs = [dir.name for dir in os.scandir(self.tmpDir) 
							if	dir.is_dir()]
		self.checkForTmpNdata()
		self.start()


	def checkForTmpNdata(self):
		if "tmp" not in os.listdir(self.mainDir):
			print("No tmp folder was found")
			exit(1)
		elif os.listdir(self.tmpDir) == []:
			print("Empty tmp folder")
			exit(1)
	
	def start(self):
		for dir in self.dirs:
			os.chdir(f"{self.tmpDir}/{dir}")
			for exec in os.listdir():
				if not exec.endswith('json'):
					print('./' + exec, "1000")
					subprocess.run(['./' + exec, "1000"])

exe = execute()