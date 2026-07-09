import os
import sys
import time
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
os.system('pip install httpx[http2]')
os.system('pip install ethan')
os.system('pip install asmix')
os.system('clear')
import requests
from user_agent import generate_user_agent
from time import time
from hashlib import md5
from random import choice
from concurrent.futures import ThreadPoolExecutor
from cfonts import render, say
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import random
import base64
import httpx
import user_agent
import ssl
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
Ex = 0

try:
    import httpx
    import user_agent
except:
    os.system("pip install httpx httpx[http2] user_agent")
    import httpx
    import user_agent

class InstagramEmailChecker:
    def __init__(self):
        self.hits = 0
        self.bads_instgram = 0
        self.bads_email = 0
        self.p1 = 0
        self.ID = ""
        self.token = ""
        self.rest = 1
        
        self.Z = '\033[1;31m'
        self.Z1 = '\033[2;31m'
        self.F = '\033[2;32m'
        self.A = '\033[2;34m'
        self.C = '\033[1;97m'
        self.J = '\033[2;36m'
        self.Y = '\033[1;34m'
        self.X = '\033[1;33m'
        self.M = '\x1b[1;37m'
        self.S = '\033[1;33m'
        self.R = '\033[1;31m'
        self.C1 = '\033[2;35m'
        self.H = '\x1b[38;5;208m'
        self.ED = '\x1b[38;5;208m'
        self.Bl = '\033[1;34m'
        self.P = '\033[1;35m'
        self.G = '\033[1;32m'
        self.N = '\033[1;37m'
        
        self.yy = 'azertyuiopmlkjhgfdsqwxcvbn'
        self.ids = []
        
    def display_banner(self):
        anuj = render('ANUJ', colors=['blue', 'white'], align='center')
        print(anuj)
        
    def tll(self):
        try:
            n1 = ''.join(cc(self.yy) for i in range(rr(6, 9)))
            n2 = ''.join(cc(self.yy) for i in range(rr(3, 9)))
            host = ''.join(cc(self.yy) for i in range(rr(15, 30)))
            he3 = {
                "accept": "*/*",
                "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
                "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                "google-accounts-xsrf": "1",
                "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
                "sec-ch-ua-arch": "\"\"",
                "sec-ch-ua-bitness": "\"\"",
                "sec-ch-ua-full-version": "\"116.0.5845.72\"",
                "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-model": "\"ANY-LX2\"",
                "sec-ch-ua-platform": "\"Android\"",
                "sec-ch-ua-platform-version": "\"13.0.0\"",
                "sec-ch-ua-wow64": "?0",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
                "x-client-data": "CJjbygE=",
                "x-same-domain": "1",
                "Referrer-Policy": "strict-origin-when-cross-origin",
                'user-agent': str(gg()),
            }

            res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
            tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
            cookies = {
                '__Host-GAPS': host
            }
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
                'user-agent': gg(),
            }
            data = {
                'f.req': '["' + tok + '","' + n1 + '","' + n2 + '","' + n1 + '","' + n2 + '",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
            }
            response = pp(
                'https://accounts.google.com/_/signup/validatepersonaldetails',
                cookies=cookies,
                headers=headers,
                data=data,
            )
            tl = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']
            try:
                os.remove('tl.txt')
            except:
                pass
            with open('tl.txt', 'a') as f:
                f.write(tl + '//' + host + '\n')
        except Exception as e:
            print(e)
            self.tll()
            
    def check_googlemail(self, email):
        if '@' in email:
            email = str(email).split('@')[0]
        try:
            try:
                o = open('tl.txt', 'r').read().splitlines()[0]
            except:
                self.tll()
                o = open('tl.txt', 'r').read().splitlines()[0]
            tl, host = o.split('//')
            cookies = {
                '__Host-GAPS': host
            }
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=' + tl,
                'user-agent': gg(),
            }
            params = {
                'TL': tl,
            }
            data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A' + tl + '%22%2C%22' + email + '%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
            response = pp(
                'https://accounts.google.com/_/signup/usernameavailability',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
            )
            print(response.text)
            if '"gf.uar",1' in str(response.text):
                return 'good'
            elif '"er",null,null,null,null,400' in str(response.text):
                self.tll()
                return self.check_googlemail(email)
            else:
                return 'bad'
        except:
            return self.check_googlemail(email)
            
    def info(self, username, jj):
        from asmix import Instagram
        try:
            url = f"https://www.instagram.com/{username}/"
            headers = {
                "User-Agent": "Mozilla/5.0"
            }
            response = requests.get(url, headers=headers)
            html = response.text
            match = re.search(r'"profile_id":"(\d+)"', html)
            user_id = match.group(1)
            response = requests.post(
                "https://www.instagram.com/graphql/query",
                headers={
                    'accept': '*/*',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': 'Mozilla/5.0',
                    'x-asbd-id': '359341',
                    'x-csrftoken': 'njXfzdB0S2d5HR-tZJ6Zfm'
                },
                data={
                    'lsd': 'AVooTjceqws',
                    'variables': f'{{"id":"{user_id}","render_surface":"PROFILE"}}',
                    'server_timestamps': 'true',
                    'doc_id': '9661599240584790'
                }
            ).json()
            user = response['data']['user']
            name = user['full_name']
            username = user['username']
            uid = user['id']
            try:
                date = Instagram.date(uid)
            except:
                date = 'None'
            posts = user['media_count']
            followers = user['follower_count']
            following = user['following_count']
            is_business = user['is_business']
            is_private = user['is_private']
            is_verified = user['is_verified']
            profile_pic = user['hd_profile_pic_url_info']['url']


            adh = f'''
────────────────────────
   NAME          ▸ {name}
   USER          ▸ {username}
   EMAIL         ▸ {username}@{jj}
   ID            ▸ {uid}
   POSTS         ▸ {posts}
   FOLLOWERS     ▸ {followers}
   FOLLOWING     ▸ {following}
   BUSINESS      ▸ {is_business}
   DATE          ▸ {date}
   REST          ▸ {self.rest}
   LINK          ▸ https://instagram.com/{username}
   
────────────────────────
  BY @PyAnuj • @itz_4nuj1
────────────────────────
   '''

            if posts >= 1:
                self.hits += 1
                requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.ID}&text={adh}")
                with open('hits.txt', "a", encoding="utf-8") as f:
                    f.write(adh + "\n")
        except Exception as e:
            adh = f"""
 Username : {username}
 Email    : {username}@{jj}
 Rest     : {self.rest}
 https://instagram.com/{username}
────────────────────────
BY :@PyAnuj • @itz_4nuj1
────────────────────────
"""
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.ID}&text={adh}")
            with open('anujhits.txt', "a", encoding="utf-8") as f:
                f.write(adh + "\n")
                
    def bmw(self, email):
        try:
            if 'good' == self.check_googlemail(email):
                username, jj = email.split('@')
                self.info(username, jj)
            else:
                self.bads_email += 1
        except:
            pass
            
    def check(self, email):
        try:
            pp_choice = choice('00')
                       
            if pp_choice == '0':
                with httpx.Client(http2=True) as client:
                    r = client.post(
                        "https://i.instagram.com/api/v1/users/check_email/",
                        data=f"email={email}",
                        headers={
                            'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",
                            'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
                        }
                    ).json()

                    if r.get('error_type') == 'email_is_taken':
                        self.bmw(email)
                    else:
                        self.bads_instgram += 1
                    os.system('clear')
                    print(f'''
────────────────────────
       HITS : {self.hits} 
       BAD MAIL : {self.bads_email}
       BAD INSTA : {self.bads_instgram}
       EMAIL : {email}  
────────────────────────                           
    ''')
        except Exception as e:
            print(f"error: {e}")
            
    def Users(self, iud, uid):
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
                'variables': '{"id":"' + str(rr(iud, uid)) + '","location_id":"","shared_entity_id":"","shid":"","skip_location":true,"skip_sharer":true,"skip_user":false}',
                'doc_id': '23907016675582737',
            }
            response = requests.post('https://www.instagram.com/graphql/query', cookies={}, headers=headers, data=data)
            user = response.json()['data']['fetch__XDTUserDict']['username']
            email = user + '@gmail.com'
            self.check(email)
        except Exception as e:
            pass
            
    def ExUsers(self, iud, uid):
        for _ in range(1000):
            self.Users(iud, uid)
            
    def run(self):
        os.system('clear')
        self.display_banner()
        
        print(f"{self.ED}╔════════════════════════════════════════╗")
        print(f"{self.ED}║         ENTER CHAT ID               ║")
        print(f"{self.ED}╚════════════════════════════════════════╝")
        self.ID = input(f"{self.ED} ==> ")
        print('')
        print(f"{self.P}╔════════════════════════════════════════╗")
        print(f"{self.P}║           ENTER TOKEN                  ║")
        print(f"{self.P}╚════════════════════════════════════════╝")
        self.token = input(f"{self.P} ==>  ")
        print('')
        wr = 1
        if wr == 1:
            pass

        os.system('clear')
        self.tll()
        os.system('clear')
        self.display_banner()
        
        print(f"""
{self.H}╔══════════════════════════════════════════════════════════╗
{self.H}║                     SELECT YEAR                          ║
{self.H}╠══════════════════════════════════════════════════════════╣
{self.H}║  {self.G}1{self.H} -  2011                                                 ║
{self.H}║  {self.G}2{self.H} - 2012                                                  ║
{self.H}║  {self.G}3{self.H} - 2013                                                  ║
{self.H}║  {self.G}4{self.H} - 2014                                                  ║
{self.H}║  {self.G}5{self.H} - 2015                                                  ║
{self.H}║  {self.G}6{self.H} - 2016-2017                                             ║
{self.H}╚══════════════════════════════════════════════════════════╝
        """)
        num = int(input(f'{self.ED}choice ==> : '))

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

        
        threads = []
        for _ in range(150):
            thread = Thread(target=self.ExUsers, args=(iud, uid))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    
    checker = InstagramEmailChecker()
    checker.run()
