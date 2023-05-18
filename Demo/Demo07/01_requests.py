import requests
r = requests.get("https://www.baidu.com")

print("=======   r.status_code")
print(r.status_code)

print("=======   r.encoding")
print(r.encoding)

print("=======   r.apparent_encoding")
print(r.apparent_encoding)

print("=======   r.text")
print(r.text)

r.encoding = r.apparent_encoding

print("=======   r.text utf-8")
print(r.text)

print("=======   r.headers")
print(r.headers)