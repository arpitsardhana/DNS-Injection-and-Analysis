import os
import sys

inp_f = str(sys.argv[1])

f = open(inp_f,'r')

f_line = f.readlines()

domain_dict = {}
lemon_dict  = {}

for line in f_line:
	entries = line.split(',')
	d_name = entries[1]
	l_ip = entries[2]
	l_ip = l_ip.rstrip()
	if d_name in domain_dict:
		domain_dict[d_name] += 1
	else :
		domain_dict[d_name] = 1
	
	if l_ip in lemon_dict:
		lemon_dict[l_ip] += 1
		
	else :
		lemon_dict[l_ip] = 1


print domain_dict
print lemon_dict


