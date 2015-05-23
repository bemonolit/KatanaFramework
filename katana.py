# KATANA Vs 0.0.0.1
# Date  : 14/05/15
# Autor : RedToor
# Tool  : Python  
# Coders: RedToor, LeSZO ZerO, cl34r 
# 
# Made in Colombia With Backtrack but for KALI ;) 
#
# KATANA Framework, Make for Kali Linux (Distribution) 
# it's Projects can be share 'd edicted, No Commerce

from scripts import TLogin
from scripts import FuzzerFTP
from scripts import BruteForcePOP3
from scripts import BruteForceSQL
from scripts import BruteForceSSH
from scripts import BruteForceFTP
from scripts import BruteRAR
from scripts import BruteZIP
from scripts import BruteForceFormBase
from scripts import BruteForceHTTP
from scripts import ClientMYSQL
from scripts import ClientFTP
from scripts import ClientPOP3
from scripts import GetDataReport
from scripts import ARPLooking
from scripts import AdminFinder
#from scripts import WifiDetecter

from core import help
from core import updatekatana


W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'

print """
	   
                  __                         __--
         ___  ___/  \_______________   ___  /  \---
         | .|/ ./ __ \__   ___/.....\  | | / __ \----
         | .  ./ /__\ \/../ _ \. /\..\ | |/ /__\ \-----
         | .| .\.\  /./../ /_\.\.\ \..\| |\.\  /./---
         |_.|\_.\.\/./._/./   \_\.\ \..__| \.\/./--
	    _______?___________________________________
	   {_| | | | I################################/
	      ^ ^ ^ ^THE FRAMEWORK, Build (0.0.0.2)
	   by """+R+"""Red"""+O+"""Toor"""+W+""", LULZ 4 u. 

	   """+R+"""Command"""+W+"""\t"""+C+"""Description"""+W+"""
	   help		: help about command
	   show modules	: modules
	   show options : options mudule
	   use		: use module
	   set          : set up 
	   update       : update Katana
	  """

def katana():
	try:
		action = raw_input(B+" KtN> "+W)
		if action == "show modules":
			print "\n 	___________________"
			print "	|web's application|"
			print "	---------------------------------------------"
			print "	|"+O+"web/httpbt"+W+"\t | "+C+"HTTP Brute Force"+W+"        |"
			print "	|"+O+"web/formbt"+W+"\t | "+C+"FORM Brute Force"+W+"        |"
			print "	|"+O+"web/cpfinder"+W+"\t | "+C+"Admin Finder"+W+"            |"
			print "	---------------------------------------------\n 	__________________"
			print "	|sniffing network|"
			print "	---------------------------------------------"
			print "	|"+O+"net/arplook"+W+"\t | "+C+"ARP Attack Detect"+W+"       |"
			print "	---------------------------------------------\n 	____________________"
			print "	|social engineering|"
			print "	---------------------------------------------"
			print "	|"+O+"seng/gdreport"+W+"\t | "+C+"Getting information"+W+"     |"
			print "	---------------------------------------------\n 	_______"
			print "	|files|"
			print "	---------------------------------------------"
			print "	|"+O+"file/brutezip"+W+"\t | "+C+"ZIP Brute Force"+W+"         |"
			print "	|"+O+"file/bruterar"+W+"\t | "+C+"RAR Brute Force"+W+"         |"
			print "	---------------------------------------------\n 	_________"
			print "	|Clients|"
			print "	---------------------------------------------"
			print "	|"+O+"clt/ftp"+W+"\t | "+C+"FTP Client"+W+"              |"
			print "	|"+O+"clt/sql"+W+"\t | "+C+"SQL Client"+W+"              |"
			print "	|"+O+"clt/pop3"+W+"\t | "+C+"POP3 Client"+W+"             |"
			print "	---------------------------------------------\n 	_______________________"
			print "	|Brute Force Protocols|"
			print "	---------------------------------------------"
			print "	|"+O+"bt/ftp"+W+"\t 	 | "+C+"FTP Brute Force"+W+"         |"
			print "	|"+O+"bt/sql"+W+"\t 	 | "+C+"SQL Brute Force"+W+"         |"
			print "	|"+O+"bt/ssh"+W+"\t 	 | "+C+"SSH Brute Force"+W+"         |"
			print "	|"+O+"bt/pop3"+W+"\t | "+C+"POP3 Brute Force"+W+"        |"
			print "	---------------------------------------------\n 	________"
			print "	|Fuzzers|"
			print "	---------------------------------------------"
			print "	|"+O+"fz/ftp"+W+"\t 	 | "+C+"FTP Fuzzer"+W+"              |"
			print "	---------------------------------------------\n 	_______________"
			print "	|Miscellaneous|"
			print "	---------------------------------------------"
			print "	|"+O+"mc/tlogin"+W+"\t | "+C+"Test of Credentials"+W+"     |"
			print "	---------------------------------------------\n                     "
			#print "	|Wifi|"
			#print "	---------------------------------------------"
			#print "	|"+O+"wifi/hwifipwd"+W+"\t | "+C+"Pwd Hacker wife"+W+"         |"
			#print "	---------------------------------------------"
			katana()
		elif action[0:3] == "use":
			if action[4:14] == "web/httpbt":
				BruteForceHTTP.httpbt()
			if action[4:16] == "web/cpfinder":
				AdminFinder.adminfinder()
			if action[4:16] == "web/formbt":
				BruteForceFormBase.httpformbasebruteforce()
			if action[4:16] == "net/arplook":
				ARPLooking.arplook()
			if action[4:17] == "seng/gdreport":
				GetDataReport.getdatareport()
			if action[4:17] == "file/brutezip":
				BruteZIP.btzip()
			if action[4:17] == "file/bruterar":
				BruteRAR.btRAR()
			if action[4:11] == "clt/ftp":
				ClientFTP.cftp()
			if action[4:10] == "bt/ftp":
				BruteForceFTP.btftp()
			if action[4:17] == "wifi/hwifipwd":
				WifiDetecter.hackerwifipwd()
			if action[4:10] == "bt/ssh":
				BruteForceSSH.btssh()	
			if action[4:11] == "clt/sql":
				ClientMYSQL.cmysql()	
			if action[4:10] == "bt/sql":
				BruteForceSQL.btsql()		
			if action[4:11] == "bt/pop3":
				BruteForcePOP3.btpop3()
			if action[4:12] == "clt/pop3":
				ClientPOP3.cpop3()
			if action[4:13] == "mc/tlogin":
				TLogin.tlogin()
			if action[4:10] == "fz/ftp":
				FuzzerFTP.fftp()
			else:
				katana()
		elif action == "exit":
			print C+"   GooD"+W+" bye."
			exit()
		elif action == "help":
			help.help()
		elif action == "update":
			updatekatana.update()
		else:
			print "[!] command No "+O+"ACCEPT"+W
			katana()
	except(KeyboardInterrupt, SystemExit):
		print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
katana()