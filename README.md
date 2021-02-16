# SmartSolutions_v2

Repository made to make life easier for passing Smart Solutions course. (Try number two, first try apparently was not successful)


RasPi MAC is --> DC:A6:32:D7:24:E8

command for getting the mac addresses and IP in the network
sudo nmap -sn 172.17.54.0/23 | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "substr($0, index($0,$3)) }' | sort

