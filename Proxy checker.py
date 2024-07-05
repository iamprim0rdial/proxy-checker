import requests

# Two List to append working ip's or not working ip's
working_ip_list = []
not_working = []

try:
    with open('proxies.txt', 'r') as f:
        for x in f.readlines():
            proxy = {
                'http': x.strip(),
                'https': x.strip()
            }
            try:
                res = requests.get('https://httpbin.org/ip', proxies=proxy, timeout=5)
                if res.status_code == 200:
                    working_ip_list.append(x.strip())
                else:
                    not_working.append(x.strip())
            except:
                not_working.append(x.strip())
except Exception as e:
    print(f"Something went wrong: {e}")
