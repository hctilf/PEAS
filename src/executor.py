import os, subprocess, psutil,time, multiprocessing, shlex

mainDir = f'/home/{os.getlogin()}/PEAS'
tmpDir = mainDir + '/tmp'
try: 
	f = open('/sys/devices/system/cpu/cpu0/cache/index3/size', 'r')
	l3 = int((f.readline().replace('K', '')))*1024
	f.close()
except FileNotFoundError:
	f = open('/sys/devices/system/cpu/cpu0/cache/index2/size', 'r')
	l3 = int((f.readline().replace('K', '')))*1024
	f.close()

class executable():
	def __init__(self, info) -> None:
		self.mem_req = int(l3/(2**info[1]+4**info[2]+8**info[3])*0.01)
		self.testing = info[0]
		self.wd = tmpDir + f'/{self.testing}'
		self.checkForTmpNdata()
		#self.start()


	def checkForTmpNdata(self):
		if "tmp" not in os.listdir(mainDir):
			print('First time, HUH?')
		elif os.listdir(tmpDir) == []:
			print("Empty tmp folder")
	
	def start(self):
		cpu_average = dict()
		os.chdir(self.wd)
		for exec in os.listdir():
			if not exec.endswith('json'):
				cmd = shlex.split(f'./{exec}'+' '+str(self.mem_req))
				sp = subprocess.Popen(cmd)
				ps = psutil.Process(sp.pid)
				cpu_percents = []
				ps.cpu_percent()

				while sp.poll() is None:
					ps.cpu_percent()
					time.sleep(0.01)
					cpu_percents.append(ps.cpu_percent())
				print(cpu_percents)
				load = sum(cpu_percents)/len(cpu_percents)
				print(exec, load)
				cpu_average.update([(exec, load)])
				cpu_percents = []
		os.chdir(tmpDir)
		return cpu_average


def execute(mem_req):
	cpu_util = dict()
	for info in mem_req:
		print('Your cpu L3 cashe size(in Bt)', l3)
		exe = executable(info)
		cpu_util.update(exe.start())
	print(cpu_util)
		
	return(cpu_util)