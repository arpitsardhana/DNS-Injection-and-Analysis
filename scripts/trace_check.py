import sys
from scapy.all import sr1,IP,UDP,DNS,DNSQR 
import os
import sys

honeyout = open(str(sys.argv[1]),'r')

trace_ttl_out = open("trace_ttl.txt",'a')

ttl_val = 2

honey_list = honeyout.read().splitlines()

for entry in honey_list:
	entry_list = entry.split(",")
	nameserv = entry_list[0]
	qry = entry_list[1]
	print nameserv
	print qry

	for ttl_val in range(14,30):	 
		p=sr1(IP(dst=nameserv,ttl=ttl_val)/UDP()/DNS(rd=1,qd=DNSQR(qname=qry)),retry=0,timeout=2)
		try:
			if p[DNS].ancount >= 1:
				#print nameserv,qry
				#trace_e = str(p[DNS][2].rdata)
				#print ttl_val
				#print tarce_e
				entry_t = nameserv+','+str(ttl_val)+','+qry
				print entry_t
				trace_ttl_out.write(entry_t)
				
				break
			else :
				print "No data found"
		except:
			continue

