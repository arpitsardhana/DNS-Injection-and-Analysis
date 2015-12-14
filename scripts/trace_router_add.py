import os
import sys
from traceroute import Traceroute

tracefile = open(str(sys.argv[1]),'r')

traceline = tracefile.readlines()
router_list = []
trace_out = open("trace_output.txt",'a')
for line in traceline:
	entry = line.split(',')
	d_name = str(entry[0])
	ttl_val = int(entry[1].rstrip())
	traceroute = Traceroute(d_name)
	print d_name
	try :
		hops = traceroute.traceroute()	
		total_hops = len(hops)
		if total_hops < ttl_val :
			out_hop = hops[total_hops-1]
			router_list.append(hops[total_hops-1])
		else :
			router_list.append(hops[ttl_val-1])
			out_hop = hops[ttl_val-1]

		output = out_hop['ip_address'] + '\n'
		trace_out.write(output)
	except:
		continue


print router_list

	
	
	
