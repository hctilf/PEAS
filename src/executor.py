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
		self.mem_req = 100000#int(l3/(2**info[1]+4**info[2]+8**info[3])*1)
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
		num = 0
		cpu_average = dict()
		os.chdir(self.wd)
		pid = os.getpgid(0) 
		for exec in os.listdir():
			if not exec.endswith('json'):
				cmd = shlex.split(f'./{exec}'+' '+str(self.mem_req))
				sp = subprocess.Popen(cmd)
				ps = psutil.Process(sp.pid)
				cpu_percents = []
				ps.cpu_percent(interval=0.01)
				ps.cpu_percent(interval=0.01)

				while sp.poll() is None:
					cpu_percents.append(ps.cpu_percent(interval=0.01))
					time.sleep(0.01)
				print(cpu_percents)
				load = sum(cpu_percents)/len(cpu_percents)
				print(exec, load)
				cpu_average.update([(exec, load)])
				cpu_percents = []
		os.chdir(tmpDir)
		return cpu_average

		
		

def time_prog(func):	#time measurement
	def wrapper(*args):
		start = time.time()
		func(*args)
		print(time.time() - start)
	return wrapper

def monitor(cmd):
	worker_process = multiprocessing.Process(target=subprocess.Popen, args=(cmd,))
	worker_process.start()
	time.sleep(1)
	for p in psutil.process_iter(['name']):
		if p.info['name'] == cmd[0]:
			ps = psutil.Process(p.pid)
	print(ps.pid)
	# log cpu usage of `worker_process` every 10 ms
	cpu_percents = []
	while worker_process.is_alive():
		print('working')
		cpu_percents.append(p.cpu_percent())
		time.sleep(0.01)
	worker_process.join()
	return cpu_percents

@time_prog
def execute(mem_req):
	utilization = []
	for info in mem_req:
		print('Your cpu L3 cashe size(in Bt)', l3)
		exe = executable(info)
		cpu_per = exe.start()
		print(cpu_per)
		
	return(cpu_per)