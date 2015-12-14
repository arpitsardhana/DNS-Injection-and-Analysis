import dns.resolver
import os
import sys

d = open(str(sys.argv[1]),'r')
ip = open(str(sys.argv[2]),'r')
domain_list = d.read().splitlines()
ip_list = ip.read().splitlines()
my_resolver = dns.resolver.Resolver()
output_f = open("output.txt",'a')
for nameserv in ip_list:
	nameserv = nameserv.replace("\n","")
	my_resolver.nameservers = [nameserv]
	for domain in domain_list: 
		try:
			domain = domain.replace("\n","")
			answer = my_resolver.query(domain).response
			#print answer.response.answer
			entry = "Querry start \n" + "server : " + "   " + nameserv + " " + "query_result " + str(answer) + "\nQuerry ends "+ '\n \n'
		        output_f.write(entry)	
		except :
			print domain,nameserv
			print "no domain"


d.close()
ip.close()
output_f.close()
