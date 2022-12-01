import os
import string

ALP = list('abcdefghklmnopqrstuvwxyz')

Name = -1

DTl = ['int', 'float', 'double']
DTd = {
	'double':'double',
	'float':'float',
	'int':'int',
	'double&':'double',
	'float&':'float',
	'int&':'int',
	'double*':'double',
	'float*':'float',
	'int*':'int',
	'double**':'double',
	'float**':'float',
	'int**':'int'
}

def put_headers(f, lib):
	headers = '#include "'+lib + '"\n#define ANKERL_NANOBENCH_IMPLEMENT\n#include <nanobench.h>\n\
#include <iostream>\n#include <cmath>\n#include <ctime>\n#include <fstream>\n\n\
using namespace std;\n\nint main(int argc, char *argv[]){\n\
	fstream file;\n\
    string json_name;\n\
    json_name.assign(argv[0]).append(".json").erase(0,2);\n\
    // cout << json_name << endl;\n\
    file.open(json_name, ios_base::out);\n\
    if (file.is_open() != true){\n\
        cout << "*Failed to open file*";\n\
        exit(0);\n\
    }\n\
	srand(time(NULL));\n\
	int size = atoi(argv[1]);\n'
	f.write(headers)

def find_headers(PATH):
    cwd = os.getcwd()
    os.chdir(PATH)
    headers = [entry.name for entry in os.scandir(os.getcwd()) if entry.name.endswith('.h') and entry.is_file() and not entry.name == 'nanobench.h']
    os.chdir(cwd)
    #for header in headers: print(header)
    return headers

def find_target(PATH, header):
	lines = []
	f = open(PATH + header, 'r')
	for line in f:
		for i in '(),;':
			line = line.replace(i, ' ')
		lines.append(line.split())
	f.close()
	return(lines)


def put_bench(f, ret, func, container, void=False):
	br, bt, var = '{', '}', '('
	for i in range(len(container)): 
		if i < len(container)-1:
			var += ''.join(str(container[i]+','))
	else: var += ''.join(str(container[i]+')'))
	funcn = '"'+func+'"'
	if not void:
		bench = f"	ankerl::nanobench::Bench().output(nullptr).warmup(11).epochs(11).run({funcn},[&] {br}\n\
			ankerl::nanobench::doNotOptimizeAway({ret} = {func}{var});\n\
		{bt}).render(ankerl::nanobench::templates::json(), file);\n"
	else:
		bench = f"	ankerl::nanobench::Bench().output(nullptr).warmup(11).epochs(11).run({funcn}, [&] {br}\n\
			{func}{var};\n\
		{bt}).render(ankerl::nanobench::templates::json(), file);\n"
	bench += '	file.close();'
	f.write(bench)

class value():
	def __init__(self, name, data_type = 'int'):
		self.dt = data_type
		global Name, ALP
		Name += 1
		self.n = name

	def put_val(self, f, name):
		self.n = name
		var = f"	{self.dt} {self.n};\n"
		f.write(var)

	def put_var(self, f):
		rand_exp = '1 + rand()%1000' if self.dt == 'int'\
				else '(float(rand())/float((RAND_MAX)) * 500.0)' if self.dt == 'float'\
				else '(double(rand())/double((RAND_MAX)) * 500.00)'
		var = f"	{self.dt} {self.n} = {rand_exp};\n"
		f.write(var)

class array(value):
	def __init__(self, name, data_type = 'int', length = 'size'):
		super().__init__(name, data_type)
		self.l = 'size'

	def put_pointer(self, f):
		pointer = f"{self.dt} *{self.n};\n"
		f.write(pointer)

	def put_array(self, f):
		rand_exp = '1 + rand()%1000' if self.dt == 'int'\
				else '(float(rand())/float((RAND_MAX)) * 500.0)' if self.dt == 'float'\
				else '(double(rand())/double((RAND_MAX)) * 500.00)'
		br, bt = '{', '}'
		gen_array = f"	{self.dt} *{self.n} = new {self.dt}[{self.l}];\n\
	for(int i = 0; i < {self.l}; i++)  {self.n}[i] = {rand_exp};\n"
		f.write(gen_array)

class matrix(array):
	def __init__(self, name, data_type='int', length = 'size', width = 'size', ):
		super().__init__(name, data_type)
		self.w = width

	def put_pointer(self, f):
		pointer = f"{self.dt} **{self.n};\n"
		f.write(pointer)

	def put_matrix(self, f):
		rand_exp = '1 + rand()%1000' if self.dt == 'int'\
				else '(float(rand())/float((RAND_MAX)) * 500.0)' if self.dt == 'float'\
				else '(double(rand())/double((RAND_MAX)) * 500.00)'
		br, bt = '{', '}'
		gen_matrix = f"	{self.dt} **{self.n} = new {self.dt}*[{self.l}];\n\
		for(int i = 0; i < {self.l}; i++){br}\n \
			{self.n}[i] = new {self.dt}[{self.w}];\n\
			for(int j = 0; j < {self.l}; j++)\n\
				{self.n}[i][j] = {rand_exp};\n\
		{bt}\n\n"
		f.write(gen_matrix)


