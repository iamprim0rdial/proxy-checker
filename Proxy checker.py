import requests
"""
AUTHOR: VISHAL 
INPUT : TXT FILE CONTAINING PROXY LIST
OUTPUT : {
            WORKING PROXY LIST 
            NON WORKING PROXY LIST
        }
"""
working = []
not_working = []

try:
    with open('YOUR_PROXY_TXT_FILE', 'r') as file:
        for ip in file.readlines():
            proxy = {
                'http': ip.strip(),
                'https': ip.strip()
            }
            try:
                response = requests.get('https://httpbin.org/ip', proxies=proxy, timeout=5)
                if response.status_code == 200:
                    working.append(ip.strip())
                else:
                    not_working.append(ip.strip())
            except:
                not_working.append(ip.strip())
except Exception as e:
    print(f"Something went wrong: {e}")
