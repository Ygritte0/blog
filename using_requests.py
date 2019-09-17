import requests
import json

# response = requests.get('http://www.baidu.com')
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)


# response = requests.get('http://httpbin.org/get')
# print(response.text)


# response = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(response.text)

# data = {
#     'name': 'germey',
#     'age': 22
# }
# response = requests.get('http://httpbin.org/get', params=data)
# print(response.text)


# response = requests.get('http://httpbin.org/get')
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))

# response = requests.get('http://github.com/favicon.ico')
# print(type(response.text), type(response.content))
# print(response.text)
# print(response.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(response.content)
#     f.close()


# response = requests.get('http://www.zhihu.com/explore')
# print(response.text)


# headers ={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
#                  ' (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
# }
# response = requests.get('http://www.zhihu.com/explore', headers=headers)
# print(response.text)

# data = {'name': 'zhaomeng', 'age': 24}
# response = requests.post('http://httpbin.org/post', data=data)
# print(response.text


# data = {'name': 'zhaomeng', 'age': 24}
# headers = {
#      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
#                   ' (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
# response = requests.post('http://httpbin.org/post', data=data, headers=headers)
# print(response.json())

# response = requests.get('http://www.jianshu.com')
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)

# response = requests.get('http://www.baidu.com')
# exit() if not response.status_code == requests.codes.ok else print('Request Successfully')

# files = {'file':open('favicon.ico', 'rb')}
# response =requests.post('http://httpbin.org/post', files=files)
# print(response.text)

# response = requests.get('http://www.baidu.com')
# print(response.cookies)
# for key, value in response.cookies.items():
#     print(key + '=' + value)

# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# from requests.packages import urllib3
# urllib3.disable_warnings()

# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)

# from requests.exceptions import ReadTimeout
# try:
#     response = requests.get('http://www.taobao.com', timeout=0.1)
#     print(response.status_code)
# except ReadTimeout:
#     print('Timeout')

# response = requests.get('http://httpbin.org/get', timeout=0.1)
# print(response.status_code)


# from requests.auth import HTTPBasicAuth
#
# r = requests.get('http://120.27.34.24:9001')
# r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', 123))
# print(r.status_code)

from requests.exceptions import ReadTimeout, ConnectionError, RequestException

try:
    response = requests.get('http://httpbin.org/get', timeout=0.5)
except ReadTimeout:
    print('Timeout')
except ConnectionError:
    print('Connection error')
except RequestException:
    print('Error')
