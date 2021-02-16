# Code imported from https://gist.github.com/DMcP89/22ac2d745e13cebe9be9
import nmap


target_mac = '18:65:90:D0:80:B1'

nm = nmap.PortScanner()

nm.scan(hosts='172.31.160.0/21', arguments='-sP')

host_list = nm.all_hosts()
for host in host_list:
	if  'mac' in nm[host]['addresses']:
		print(host+' : '+nm[host]['addresses']['mac'])
#                if target_mac == nm[host]['addresses']['mac']:
#                        print('Target Found')
