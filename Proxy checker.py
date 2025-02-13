import requests

# Two List to append working ip's or not working ip's
working = []
not_working = []

try:
    with open('proxies.txt', 'r') as file:
        for ip in file.readlines():
            proxy = {
                'http': ip.strip(),
                'https': ip.strip()
            }
            try:
                res = requests.get('https://httpbin.org/ip', proxies=proxy, timeout=5)
                if res.status_code == 200:
                    working.append(ip.strip())
                else:
                    not_working.append(ip.strip())
            except:
                not_working.append(ip.strip())
except Exception as e:
    print(f"Something went wrong: {e}")
