import math
import csv
from netaddr import *
import pprint
import math
import socket,struct
import sys
input_file = str(sys.argv[1])

file_open = open(input_file,'r')

bin_8 = '10000'

filename = "output"

output = open(filename,'w')

with open(input_file,'rb') as f:
	for row in csv.reader(f,delimiter=',',skipinitialspace=True):
		temp = row
		if temp[0] == "" or temp[0].replace(" ","") == "":
			continue
		add_start = row[0]
		add_end = row[1]
		no_of_add = int(row[2])


		ip_add = IPAddress(add_start)
		no_of_gen_add = no_of_add/16

		for i in range(0,no_of_gen_add):

                        writen = add_start + '\n'
	                output.write(writen)

			add_bin = ip_add.bin

			bin_add = int(add_bin,2)+int(bin_8,2)
			
			add_start = socket.inet_ntoa(struct.pack('!L', bin_add))
			ip_add = IPAddress(add_start)
			

			
		


		

