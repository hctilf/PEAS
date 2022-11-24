import os
import string
import sys
from generator_classes import *



def main():
	int_cnt, flt_cnt, dp_cnt = 0, 0, 0
	for h in find_headers(sys.argv[0]):
		for f in find_target(sys.argv[0], h):
			file = open('test'+(f[1][2::] if f[1][:2] == '**' \
						else f[1][1::] if f[1][0] == '*'\
						else f[1])+'.cpp', 'w')
			put_headers(file, h)
			vars = ['size']
			print(len(f))
			for i in range(3, len(f)):
			#print (f[i])
				if f[i] in DTl:
					c = value(ALP[i-2], f[i])
					c.put_var(file)
					vars.append(c.n)

				if f[i].endswith('&'):
					c = value(ALP[i-2], DTd[f[i]])
					c.put_val(file, c.n)
					vars.append(c.n)

				if f[i].endswith('**'):
					c = matrix(ALP[i-2], DTd[f[i]])#, ALP[i-4], ALP[i-3], f[i-1])
					c.put_matrix(file)
					vars.append(c.n)

				elif f[i].endswith('*'):
					print(ALP[i-2]!=f[1][:2], f[1][:1])
					c = array(ALP[i-2].upper() if ALP[i-2]!=f[1][:2] else ALP[i-2], DTd[f[i]])#, ALP[i-4], f[i-1])
					c.put_array(file)
					vars.append(c.n)
			print(f[0])
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

if __name__ == '__main__':
	main()