import socket
from urllib import request, parse, error
import urllib
import http.cookiejar
from urllib.parse import urlparse, urlunparse, urljoin, urlencode

# response = urllib.request.urlopen('http://www.python.org')
# print(response.read().decode('utf-8'))
#
#
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())
#
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# response = urllib.request.urlopen('http://www.python.org')
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


# request = urllib.request.Request('http://www.python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# url = 'http://httpbin.org/post'
# headers = {
#     "User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 '
#                   'Safari/537.36',
#     "Host": 'httpbin.org'
# }
# dict = {
#     'name': 'Germany'
# }
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


# proxy_handler = urllib.request.ProxyHandler({
#     'http://127.0.0.1:9743',
#     'http://127.0.0:9743'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())

#
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)


# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.URLError as e:
#     print(e.reason)


# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# try:
#     response = request.urlopen('http://baidu.com', timeout=0.01)
# except error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result)


# result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result)
#
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# print(result)

# data = ['http','wwww.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))
#
# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'http://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'http://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'http://cuiqingcai.com/FAQ.html?question=2'))


# params = {
#     'name':'zhaomeng',
#     'age': 24
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)