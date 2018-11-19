#!/usr/bin/python

# I LOVE PYTHON(^-^)
# A Python Tool For Send Anonymously Email :)
# Coded By : OseidAldary
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## IMPORT LIBRARIES..:)
try:
   import mechanize
except ImportError:
	print('\n[!] Error: The [ Mechanize ] Library Is Not Installed !\n[*] Please Install It Use This Command: pip install mechanize')
	exit(1)
import optparse,socket
from time import sleep
from random import randint
from os import system as sy
## Done!
sy("cls||clear")
rd = '\033[1;31m'
gr = '\033[1;32m'
yl = '\033[1;33m'
wi = '\033[1;37m'

## Done!

## Random Proxy For Use..:)

def proxy(): # Default Proxy List

	p1 = "185.53.179.29:80" #netherlands
        p2 = "162.255.119.250:80" #US
	p3 = "193.111.63.208:80" #netherlands
      	p4 = "104.28.20.2:80" #US
	p5 = "62.210.105.242:80" #FR
	p6 = "162.255.119.250:80" #US
	p7 = "103.224.212.222:80" #UK
	p8 = "104.28.20.2:80" #US
	p9 = "93.191.169.211:80" #UK
	p10 = "69.64.147.10:80" #US
	p11 = "62.149.128.160:80" #netherlands
	p12 = "46.4.207.219:80" #FR

	proxys = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
	randproxy = proxys[randint(0,11)]
	return randproxy
randproxy = proxy()
## Check Internet Connection..:)
server = "www.google.com"
def check():
  try:
     ip = socket.gethostbyname(server)
     con = socket.create_connection((ip, 80), 2)
     return True
  except:
	pass
  return False

## Done !

## Tool Banner
banner = gr+'''
  ___                         ___  ___          
 / _ \       @Anonymously     |  \/  |          
/ /_\ \_ __   ___  _ __  _   _| .  . |___  __ _ 
|  _  | '_ \ / _ \| '_ \| | | | |\/| / __|/ _` |
| | | | | | | (_) | | | | |_| | |  | \__ \ (_| |
\_| |_/_| |_|\___/|_| |_|\__, \_|  |_/___/\__, |
                          __/ |            __/ |
Send Anonymously Email:) |___/ by:JOKER11 |___/ 
================================================
'''
###

### Usage Msg
parse = optparse.OptionParser(banner+wi+'''
Usage: python ./AnonyMsg.py [OPTIONS...]
----------------------------------------
OPTIONS:
       |
    |--------
    | -r --recipient ::> recipient address?
    |--------
    | -s --subject   ::> subject Of Email?
    |--------
    | -m --message   ::> set your message
    |--------
    | -d --def-porxy ::> Use Random Proxy From Default Script Proxy list
    |--------
    | -u --use-proxy ::> Use Select Porxy From User
-------------
EXAMPLES:
        |
     |----------
     | python AnonyMsg.py -r oseid@gmail.com -s Hacking -m 'Your Have Been Hacked!'
     |----------
     | python AnonyMsg.py -r oseid@gmail.com -s Hacking -m 'Your Network is Hacked!' --def-proxy
     |----------
     | python AnonyMsg.py -r oseid@gmail.com -s Hacking -m 'Your Server Is Hacked' -u 31.155.3.222:80
     |----------
''')
## Create Main Function..:)
def Main():
	parse.add_option('-r','--recipient',dest='recaddr',type='string')
	parse.add_option('-s','--subject',dest='subject',type='string')
        parse.add_option('-m','--message',dest='msg',type='string')
	parse.add_option('-d','--def-proxy',action='store_true',dest='prox',default=False)
	parse.add_option("-u","--use-proxy",dest="proxyis",type="string")

	(options,args) = parse.parse_args()

	## Start
	def useproxy():
	  if options.prox:
		return True
	  else:
		return False

	useproxy = useproxy()

	if options.recaddr !=None and options.subject !=None and options.msg !=None:
		to = options.recaddr
		sub = options.subject
		msg = options.msg
		if check() == True:
                 br = mechanize.Browser()
	         url = "http://anonymouse.org/anonemail.html"
                 useuser = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
                 br.addheaders = [('User-agent', useuser)]
		 if useproxy == True:
			br.set_proxies({"https":randproxy})
	         elif options.proxyis !=None:
                    proxyis = options.proxyis
                    if ":" in proxyis:
		       print(wi+"\n["+yl+"~"+wi+"]"+gr+" Connecting To Proxy["+wi+proxyis+gr+"]...")
                       proxy = proxyis.split(":")
                       proxy,port = proxy[0],int(proxy[1])
                       try:
                          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                          s.settimeout(5)
                          s.connect((proxy, port))
                          s.close()
                          br.set_proxies({"https":proxyis})
			  print(wi+"["+gr+"+"+wi+"]"+gr+" Connected :)")
                       except socket.error:
                           print(rd+"\n["+yl+"!"+rd+"]"+yl+" Connection Failed TO Proxy[ "+rd+proxy+":"+str(port)+yl+" ]"+rd+" !!!")
                           print(wi+"["+yl+"!"+wi+"]"+yl+" Please Try Other Proxy\n"+wi+"["+yl+"!"+wi+"]"+yl+" Select The Proxy Use Port"+wi+"["+yl+"80"+wi+"]"+yl+" And "+wi+"["+yl+"HTTPS"+wi+"]"+yl+" Is "+gr+"Active")
                           exit(1)
                    else:
                        print(wi+"\n["+yl+"!"+wi+"]"+yl+" Please Set A Proxy With Port Like This"+wi+"[ "+yl+"31.155.3.222:80"+wi+" ]")
                        exit(1)
                 br.set_handle_equiv(True)
                 #br.set_handle_gzip(True)
                 br.set_handle_redirect(True)
                 br.set_handle_referer(True)
                 br.set_handle_robots(False)
                 br.set_debug_http(False)
                 br.set_debug_redirects(False)
                 br.open(url)
		 br.select_form(nr=0)
		 br.form['to'] = to
		 br.form['subject'] = sub
		 br.form['text'] = msg
		 result = br.submit()
		 response = br.response().read()
		 if useproxy == True:
			proxystatus = gr + randproxy +wi+'['+gr+'ON'+wi+']'
	         elif options.proxyis !=None:
                    proxyis = options.proxyis
                    proxystatus = gr + proxyis +wi+'['+gr+'ON'+wi+']'
		 else:
			proxystatus = yl+'['+rd+'OFF'+yl+']'
		 print(' ')
		 print(rd+'='*10+gr+'> Config <'+rd+'='*10)
		 print(wi+"[R] RECIPIENT    :> "+gr+to)
		 sleep(0.30)
		 print(wi+'[S] Subject      :> '+gr+sub)
		 sleep(0.30)
		 print(wi+'[M] Message      :> '+gr+msg)
		 sleep(0.30)
		 print(wi+"[P] ProxyStatus  :> "+proxystatus)
		 print(rd+"="*30)
		 sleep(0.30)
		 print(gr+'\n['+yl+'~'+gr+'] '+wi+'Sending Msg To[ '+yl+to+wi+' ] '+gr+'...')
		 sleep(2.5)
   		 if "The e-mail has been sent anonymously!" in response:
			print(gr+"\n["+wi+"#"+gr+"]"+yl+" The Email Has Been Sent Anonymously TO[ "+gr+to+yl+" ] :)")
			print(gr+'['+wi+'>'+gr+']'+wi+' The Recipient Will Get The Email In Up To 12 Hours')
		 else:
		      print(rd+'\n['+yl+'!'+rd+'] '+yl+"Failed To Send Email To[ "+rd+to+yl+" ]"+rd+" :(!")
		      print(rd+'['+yl+'!'+rd+'] '+yl+'Try Again Later!'+rd+'[ '+yl+'OR'+rd+' ] '+wi+'Using '+gr+'['+wi+'Proxy'+gr+']'+wi+' OPTIONS')	      

                else:
		     print(yl+"\n[!] "+gr+'Error Your Not Connected To [ '+rd+'INTERNET'+gr+' ]!\n[#] Please Connect To Internet And Try Again :)')
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
