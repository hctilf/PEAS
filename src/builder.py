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
	subprocess.check_output(['bash', 'g++ -I. lsm.cpp testcubik.cpp -O0 -o testcubik-O0'])
	#optim = 'OPTIMIZATION = ' + ' '.join(OPTIMISATION) + '\n'
	#for file in find_files():
		#for oX in OPTIMISATION:
		#	print(' '.join([COMP, file, lib, 'I' + NANOBENCH,\
		#	oX, '-o', file[:len(file)-4]+oX]))
		#	subprocess.check_output(['bash', '-c', ' '.join([COMP, file, lib, 'I' + NANOBENCH,\
		#	oX, '-o', file[:len(file)-4]+oX])])
	print(src)

			
def main():
	build('lsm.cpp')


if __name__ == '__main__':
	main()