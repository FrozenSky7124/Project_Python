import requests
r = requests.get("https://www.baidu.com")

r.status_code
r.encoding
r.apparent_encoding
r.text

r.encoding = r.apparent_encoding

r.headers

#
# Get HTML Text
#

import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status() # throw HTTPError if not 200
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "HTTPError"

if __name__ == "__main__":
    url = "www.google.com"
    print(getHTMLText(url))

#
# POST request
#

import requests

payload = {
    'key1': 'value1',
    'key2': 'value2'
}

r = requests.post("http://httpbin.org/post", data = payload)

r = requests.post("http://httpbin.org/post", data = "ABC")

#
# Requests Method
#

import requests

kv = {
    'key1': 'value1',
    'key2': 'value2'
}

#   - params  �ֵ䡢�ֽ����У���Ϊ�������ӵ�url��
r = requests.request('GET', "http://python123.io/ws", params = kv)

print(r.url)

#   - data    �ֵ䡢�ֽ����С��ļ�������Ϊ Request �����ݣ���Ҫ������������ύ��Դ
r = requests.request('POST', "http://python123.io/ws", data = kv)
r = requests.request('POST', "http://python123.io/ws", data = "�ַ�������")

#   - json    JSON��ʽ�����ݣ���Ϊ Request ������
r = requests.request('POST', "http://python123.io/ws", json = kv)

#   - headers �ֵ䣬HTTP����ͷ��ģ�� Chrome/10 �������������
hd = {'user-agent': 'Chrome/10'}
r = requests.request('POST', "http://python123.io/ws", headers = hd)

#   - files   �ֵ����ͣ������ļ�
fs = {'file': open('data.xls', 'rb')}
r = requests.request('POST', "http://python123.io/ws", files = fs)

#   - proxies �ֵ����ͣ��趨���ʴ�����������������ӵ�¼��֤
pxs = {
    'http': 'http://user:pass@10.10.10.1:1234',
    'https': 'https://10.10.10.1:4321'
}
r = requests.request('GET', "http://www.google.com", proxies = pxs)

