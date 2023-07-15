#!/usr/bin/env python3
import requests
import os
import re
import time
import random
from requests.exceptions import RequestException

# DESIGN OF THE TOOL                                              
# Coded By Mr.Toxic 
os.system("clear")
#-------------------------------------------------------------------

print("""\033[1m                                          
\033[31m⌌\033[32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[31m⌍          
▏\033[36mTool Name : \033[33mMR.FACEBOOK \033[31m    ▕              
▏\033[36mAuthor    : \033[33mMr.Mandeep \033[31m     ▕              
▏\033[36mWOT       : \033[33mFBMulti_Post\033[31m    ▕
▏\033[36mType      : \033[33mPremuim \033[31m        ▕                
⌎\033[32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[31m⌏                        """)

while True:
    try:
        print()
        if os.path.exists("cookie.txt"):
            print("\033[1m\033[33m[\033[36m¥\033[33m]\033[32m One Cookie Found.")
            with open("cookie.txt", "r") as f:
                cookies = f.read()
                opt = input("\033[33m\033[1m[\033[36m¥\033[33m] \033[32mDo you want to use this Cookie [y/n] : \033[36m")
                print("\033[33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                if opt.lower() == "y":
                    cookies = input("\033[31m[\033[32m+\033[31m] \033[1m\033[33mYour FB Cookie:👇\n\033[33m━━━━━━━━━━━━━━━━━━━━━━━\033[36m\n" + cookies)
                    print("\033[33m━━━━━━━━━━━━━━━━━━━━━━━")
                elif opt.lower() == "n":
                    os.system("python cookie.py")
                else:
                    print("\033[32m[\033[31mx\033[32m] \033[31mWrong Input. Try Again.")
                    time.sleep(2)
                    os.system("python main.py")
        else:
            os.system("python cookie.py")

        try:
            response = requests.get('https://business.facebook.com/business_locations', headers={
                'Cookie': cookies,
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
            }).text
            token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
        except AttributeError:
            print(f"\033[32m[\033[31m?\033[32m] \033[32mSending Response...")
            break

        id_post = int(input("\033[32m[\033[31m+\033[32m] \033[33mENTER POST ID : \033[32m"))
        delay = int(input("\033[32m[\033[31m!\033[32m] \033[33mDELAY : \033[32m"))

        with open("/storage/emulated/0/Token/S4CH1N XD.txt", "r") as f:
            comments = f.readlines()

        x, y = 0, 0
        print("                                   ")
        # ...

while True:
    # ...
    
    x, y = 0, 0
    print("                                   ")
    while True:
        try:
            time.sleep(delay)
            teks = random.choice(comments).strip()
            data = {
                'message': teks,
                'access_token': token_eaag
            }
            response2 = requests.post(f'https://graph.facebook.com/{id_post}/comments/', data=data, cookies={
                'Cookie': cookies,
            }).json()
            if 'id' in response2:
                x += 1
                print(f"""\033[35m[{x}] \033[32mStatus : \033[32mSuccess\033[36m
[/]Link : https://mbasic.facebook.com/{id_post}
[/]Comments : {teks}
""")
            else:
                y += 1
                print(f"""\033[35m[{y}] \033[32mStatus : \033[31mFailure\033[36m
[/]Link : https://mbasic.facebook.com/{id_post}
[/]Comments : {teks}
""")
                continue

            # Add a delay after each comment
            time.sleep(delay)

        except RequestException:
            print("[!] Error Connection...", end='\r')
            time.sleep(5.5)
            continue

    # ...
