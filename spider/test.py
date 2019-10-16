


import requests,random

proxies = [
    '115.224.163.58:61202',
    '177.37.166.164:20183',
    '217.61.106.183:80',
    '103.88.140.85:8080',
    '95.0.219.105:8080',
    '188.211.227.253:53281'
]

keyword = '动漫头像'
session = requests.Session()

# cookies的获取和设置
res = requests.get(url='https://www.baidu.com')
print(res.cookies.items()) #[('BDORZ', '27315')]
res.cookies.set('cookie-name','cookie-value')
cookies = res.cookies.get('cookie-name')
print(cookies)#cookie-value



