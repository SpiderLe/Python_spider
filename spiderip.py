#IP地址归属地自动查询

import requests

url = 'http://m.ip138.com/ip.asp?ip='
ip = '202.204.80.112'

try:
    r = requests.get(url + ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("Error!")
