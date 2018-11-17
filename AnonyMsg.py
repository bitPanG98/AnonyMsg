#!/usr/bin/python

# I LOVE PYTHON(^-^)
# A Python Tool For Send Anonymously Email :)
# Coded By : OseidAldary
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## IMPORT LIBRARIES..:)
try:
   import mechanize
except:
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

def proxy():

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
 / _ \       @Anonymousl      |  \/  |          
/ /_\ \_ __   ___  _ __  _   _| .  . |___  __ _ 
|  _  | '_ \ / _ \| '_ \| | | | |\/| / __|/ _` |
| | | | | | | (_) | | | | |_| | |  | \__ \ (_| |
\_| |_/_| |_|\___/|_| |_|\__, \_|  |_/___/\__, |
                          __/ |            __/ |
Send Anonymously Email:) |___/            |___/ 
================================================
'''
###

### Usage Msg
parse = optparse.OptionParser(banner+wi+'''
Usage: python ./AnonyMsg.py [OPTIONS...]

OPTIONS:
	-r --recipient ::> recipient address?

	-s --subject   ::> subject Of Email?

	-m --message   ::> set your message

	-p --use-porxy ::> If You Want Use Proxy With Sent The Email
EXAMPLES:

./AnonyMsg.py -r oseid@gmail.com -s Hacking -m 'Your Have Been Hacked!'
./AnonyMsg.py -r oseid@gmail.com -s Hacking -m 'Your Have Been Hacked!' -p


''')
## Create Main Function..:)
def Main():
	parse.add_option('-r','--recipient',dest='recaddr',type='string')
	parse.add_option('-s','--subject',dest='subject',type='string')
        parse.add_option('-m','--message',dest='msg',type='string')
	parse.add_option('-p','--use-proxy',action='store_true',dest='prox',default=False)

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
                 br.open(url)
                 br.set_handle_equiv(True)
                 br.set_handle_gzip(True)
                 br.set_handle_redirect(True)
                 br.set_handle_referer(True)
                 br.set_handle_robots(False)
                 br.set_debug_http(False)
                 br.set_debug_redirects(False)
		 br.select_form(nr=0)
		 br.form['to'] = to
		 br.form['subject'] = sub
		 br.form['text'] = msg
		 result = br.submit()
		 response = br.response().read()
		 if useproxy == True:
			proxystatus = yl + randproxy +rd+'['+gr+'ON'+rd+']'
		 else:
			proxystatus = '['+rd+'OFF'+wi+']'
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
		 print(yl+'\n[$]'+wi+'Sending Msg To[ '+rd+to+wi+' ] '+rd+'....')
		 sleep(2.5)
   		 if "The e-mail has been sent anonymously!" in response:
			print(gr+"\n[#]"+yl+" The Email Has Been Sent Anonymously TO[ "+rd+to+yl+" ] :)")
			print(gr+'[>]'+wi+' The Recipient Will Get The Email In Up To 12 Hours')
		 else:
		      print(rd+'\n[x] '+wi+"Failed To Send Email To[ "+yl+to+wi+" ] :(")
		      print(rd+'[#] '+gr+'Try Again Later![ OR ] Try[ '+yl+'-p '+gr+' ] To Use Proxy :)')

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

