#使用requests模块与Web应用进行交互

import requests

r = requests.get('https://bjw.halodigit.com:9060/nereus/agent/v/#/login')
print("内容：",r.text)
print("状态码：",r.status_code)
print("响应头域：")
for i in r.headers.items():
    print(i)
