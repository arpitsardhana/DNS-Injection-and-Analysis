import sys
import os


filename = str(sys.argv[1])
out = open(filename,'r')
l = out.readlines()
honeyquery = open("honeyQuerryOutput",'w')
i = 0
while i < len(l):
	line = l[i].split()
	if "start" in line:
		i += 1
		line = l[i].split()
		server = line[2]
		i = i+5
		line = l[i].split()
		domain = line[0].replace("com.","com")
		lemonlist = list()
		#print server,domain,line

		i += 2
		line = l[i].split()
		if "IN" in line and "A" in line:
                       	lemonlist.append(line[len(line)-1])
                       	i = i+ 1
                       	line = l[i].split()
		else :
			i = i+1
			line = l[i].split()
	
		while "IN" in line and "A" in line:
			lemonlist.append(line[len(line)-1])
			i = i+ 1
			line = l[i].split()
	
		for item in lemonlist:
			entry = server+','+domain+','+item+'\n'
			honeyquery.write(entry)

	i += 1
	if (i > len(l) -10):
		break
			
