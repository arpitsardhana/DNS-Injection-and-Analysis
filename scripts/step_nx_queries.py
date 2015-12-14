import dns.resolver
import os
import sys
import random
import string

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
		#try:
			#domain = domain.replace("\n","")
			domain_append = list()
			domain_parts = domain.split(".")
			if len(domain_parts) < 3:
				continue
		        dom = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
			str1 = domain
			str2 = domain_parts[1] + '.' +domain_parts[2]
			str3 = dom+str2
			str4 = dom +'.'+str2
			str5 = str2+'.'+dom
			domain_append.append(str1)
                        domain_append.append(str2)
                        domain_append.append(str3)
                        domain_append.append(str4)
                        domain_append.append(str5)
			print domain	
			print domain_append
			for item in domain_append:
				try:
					answer = my_resolver.query(item).response
					#print answer.response.answer
					entry = "Querry start \n" + "server : " + "   " + nameserv + " " + "query_result " + str(answer) + "\nQuerry ends "+ '\n \n'
		        		output_f.write(entry)	
				except :
					print item,nameserv
					print "no domain"
					continue


d.close()
ip.close()
output_f.close()
