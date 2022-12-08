import string
import sys
from generator_classes import *



def generator(PATH):
	mem_req = []
	for h in find_headers(PATH):
		for f in find_target(PATH, h):
			int_arr, flt_arr, dp_arr = 0, 0, 0
			int_cnt, flt_cnt, dp_cnt = 0, 0, 0
			name = ('test' + (f[1][2::] if f[1][:2] == '**' \
					else f[1][1::] if f[1][0] == '*'\
					else f[1]))
			file = open( name + '.cpp', 'w')
			put_headers(file, h)
			vars = ['size']
			for i in range(3, len(f)):
				if f[i] in DTl:
					c = value(ALP[i-2], f[i])
					c.put_var(file)
					vars.append(c.n)
					int_cnt += 1 if f[i].startswith('int') else 0
					flt_cnt += 1 if f[i].startswith('flo') else 0
					dp_cnt += 1 if f[i].startswith('dou') else 0

				if f[i].endswith('&'):
					c = value(ALP[i-2], DTd[f[i]])
					c.put_val(file, c.n)
					vars.append(c.n)

				if f[i].endswith('**'):
					c = matrix(ALP[i-2], DTd[f[i]])#, ALP[i-4], ALP[i-3], f[i-1])
					c.put_matrix(file)
					vars.append(c.n)
					int_arr += 2 if f[i].startswith('int') else 0
					flt_arr += 2 if f[i].startswith('flo') else 0
					dp_arr += 2 if f[i].startswith('dou') else 0

				elif f[i].endswith('*'):
					c = array(ALP[i-2].upper() if ALP[i-2]!=f[1][:2] else ALP[i-2], DTd[f[i]])#, ALP[i-4], f[i-1])
					c.put_array(file)
					vars.append(c.n)
					int_arr += 1 if f[i].startswith('int') else 0
					flt_arr += 1 if f[i].startswith('flo') else 0
					dp_arr += 1 if f[i].startswith('dou') else 0
			if f[0] != 'void':
				c = value((f[1][2::][0] if f[1].startswith('**')\
				else f[1][1::][0] if f[1].startswith('*')\
				else f[1][0])+'__', f[0])
				c.put_val(file, c.n)
				put_bench(file, c.n, (f[1][2::] if f[1].startswith('**') \
				else f[1][1::] if f[1].startswith('*')\
				else f[1]), vars)
			else: put_bench(file, (f[1][2::][0] if f[1].startswith('**')\
				else f[1][1::][0] if f[1].startswith('*')\
				else f[1][0])+'__', (f[1][2::] if f[1][:2] == '**' \
				else f[1][1::] if f[1][0] == '*'\
				else f[1]), vars, True)
			file.write('\n}')
			mem_req.append([name, int_arr, flt_arr, dp_arr, int_cnt,\
			flt_cnt, dp_cnt])
	return mem_req

#if __name__ == '__main__':
#	main()