import os, subprocess

f = open('/sys/devices/system/cpu/cpu0/cache/index3/size', 'r')
l3 = int((f.readline().replace('K', '')))*1024
f.close()


class executable():
	def __init__(self, id, info) -> None:
		self.mem_req = int(l3/(2**info[1]+4**info[2]+8**info[3])*0.1)
		self.id = id
		self.testing = info[0]
		self.mainDir = f'/home/{os.getlogin()}/PEAS'
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
				subprocess.run(['./' + exec, '100'])#str(self.mem_req)
		os.chdir(self.tmpDir)

def execute(mem_req):
	for id, info in enumerate(mem_req):
		print('Your cpu L3 cashe size(in Bt)', l3)
		exe = executable(id, info)
		print('Current executable n = ', exe.mem_req)
		

#exe = execute()