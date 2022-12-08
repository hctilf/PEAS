import os, sys, subprocess, psutil, threading
from  generator import *
#generator needs one additional argument: .h file parent directory
#subprocess.run(['python3', 'generator.py', '/home/majong/PEAS/src/'])

f = open('/sys/devices/system/cpu/cpu0/cache/index3/size', 'r')
l3 = int((f.readline().replace('K', '')))*1024
f.close()
print(l3)
mem_req = generator('/home/vadim/PEAS/src/')

#generator needs one additional argument: first is path to library sources, the second one is parent directory to testSOMETHING.cpp 
#subprocess.run(['python3', 'builder.py', '/home/majong/PEAS/src/lsm.cpp', '/home/majong/PEAS/src/'])


class execute():
	def __init__(self, id, folder) -> None:
		self.mem_req = int(l3/(2**mem_req[id][1]+4**mem_req[id][2]+8**mem_req[id][3]))
		self.id = id
		self.testing = folder
		self.mainDir = os.path.split(os.getcwd())[0]
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

def main():
	for id, dir in enumerate(mem_req):
		print('Your cpu L3 cashe size(in Bt)', l3)
		exe = execute(id, mem_req[id][0])
		print('Current executable n = ', exe.mem_req)
		

if __name__ == "__main__":
	main()
#exe = execute()