import os, sys, subprocess, psutil, threading
from  generator import *
#generator needs one additional argument: .h file parent directory
#subprocess.run(['python3', 'generator.py', '/home/majong/PEAS/src/'])

f = open('/sys/devices/system/cpu/cpu0/cache/index3/size', 'r')
l3 = int((f.readline().replace('K', '')))*1024
f.close()
mem_req = generator(os.getcwd()+'/src/')

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
	def __init__(self, id, folder) -> None:
		self.mem_req = int(l3/(2**mem_req[id][1]+4**mem_req[id][2]+8**mem_req[id][3]))
		self.id = id
		self.testing = folder
		self.mainDir = os.getcwd()
		print(self.mainDir)
		self.tmpDir = self.mainDir + '/tmp'
		self.wd = self.tmpDir + f'/{self.testing}'
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
		os.chdir(self.wd)
		for exec in os.listdir():
			if not exec.endswith('json'):
				print('./' + exec, self.mem_req)
				subprocess.run(['./' + exec, str(self.mem_req)])
		os.chdir(self.tmpDir)

exe = execute()