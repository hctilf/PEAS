import os
import subprocess

COMP = 'g++'
OPTIMISATION = ['-O0', '-O1', '-O2', '-O3', '-Ofast']
NANOBENCH = '.'

def find_files():
	files = [entry.name for entry in os.scandir(os.getcwd()) if entry.name.startswith('test') and entry.name.endswith('.cpp') and entry.is_file() and not entry.name == 'nanobench.h']
	for f in files: print(f)
	return files

def build(lib):
	src = 'SRCMODULES = ' + ' '.join(find_files()) + '\n'
	#subprocess.run(['g++', '-I.', 'lsm.cpp', 'testcubik.cpp', '-O0',\
	#	 '-o testcubikO0'])
	optim = 'OPTIMIZATION = ' + ' '.join(OPTIMISATION) + '\n'
	for file in find_files():
		for oX in OPTIMISATION:
			print(COMP, '-I'+NANOBENCH, lib, file,\
			oX, '-o', file[:len(file)-4]+oX[1:])
			subprocess.run([COMP, '-I'+NANOBENCH, lib, file,\
				oX, '-o', file[:len(file)-4]+oX[1:]])
	print(src)

			
def main():
	build('lsm.cpp')


if __name__ == '__main__':
	main()