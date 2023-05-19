import requests

kv = {
    'key1': 'value1',
    'key2': 'value2'
}

#   - params  字典、字节序列，作为参数增加到url中
r = requests.request('GET', "http://python123.io/ws", params = kv)

print(r.url)

#   - data    字典、字节序列、文件对象，作为 Request 的内容，主要用作向服务器提交资源
r = requests.request('POST', "http://python123.io/ws", data = kv)
r = requests.request('POST', "http://python123.io/ws", data = "字符串内容")

#   - json    JSON格式的数据，作为 Request 的内容
r = requests.request('POST', "http://python123.io/ws", json = kv)

#   - headers 字典，HTTP定制头（模拟 Chrome/10 浏览器发起请求）
hd = {'user-agent': 'Chrome/10'}
r = requests.request('POST', "http://python123.io/ws", headers = hd)

#   - files   字典类型，传输文件
fs = {'file': open('data.xls', 'rb')}
r = requests.request('POST', "http://python123.io/ws", files = fs)

#   - proxies 字典类型，设定访问代理服务器，可以增加登录认证
pxs = {
    'http': 'http://user:pass@10.10.10.1:1234',
    'https': 'https://10.10.10.1:4321'
}
r = requests.request('GET', "http://www.google.com", proxies = pxs)
