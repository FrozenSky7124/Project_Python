#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/hangj/ddns
# https://www.dnspod.cn/docs/index.html
# https://www.cnblogs.com/hangj/p/14942691.html

import os, sys, platform
import json, gzip, time
from urllib import request, parse


# '$ID,$Token'
login_token = '******,********************************'
domain, sub_domain = 'example.com', '@'

# os.environ["LOGIN_TOKEN"]
# os.environ["DOMIN"], os.environ["SUB_DOMIN"]


def checkResponse(func):
    def wrappedFunc(*args, **kwargs):
        res = func(*args, **kwargs)
        if int(res['status']['code']) != 1: eprint(func.__name__, res)
        return res
    return wrappedFunc


def REQ(url, params=None, headers=None):
    headers = headers or {}
    if params: # dict
        params = json.dumps(params) if headers.get('Content-Type') and 'application/json' in headers['Content-Type'] else parse.urlencode(params)
        params = params.encode('utf-8')
        
    # 当 params 不为空，method 为 POST
    req = request.Request(url, params, headers)
    with request.urlopen(req, timeout=60) as page:
        res = page.read()

        if page.getheader('Content-Encoding') == 'gzip':
            res = gzip.decompress(res).decode('utf-8')
        else:
            res = res.decode('utf-8')

        if 'application/json' in page.getheader('Content-Type').lower():
            res = json.loads(res)

        return res


@checkResponse
def getRecordLine(login_token, domain):
    # 如果域名等级没有变更，则每次返回的允许的线路都是一致的，建议获取成功后在本地保存一份, 不要用一次就请求一次
    # line_ids 为新增的返回字段，对应关系为: 中文线路名称：线路ID，支持在创建、修改解析记录的时候传入线路ID，解决之前部分开发者存在的中文编码问题
    # curl -X POST https://dnsapi.cn/Record.Line -d 'login_token=LOGIN_TOKEN&format=json&domain_grade=D_Free&domain_id=2059079'
    url = "https://dnsapi.cn/Record.Line"
    params = {
        'login_token': login_token,
        'format': 'json',
        'domain': domain,
        'domain_grade': 'D_Free',
    }
    return REQ(url, params)


@checkResponse
def getRecordList(login_token, domain, sub_domain):
    # curl -X POST https://dnsapi.cn/Record.List -d 'login_token=1234,abcd&format=json&domain=yourdomain.com&sub_domain=ddns&record_type=A&offset=0&length=3'
    url = "https://dnsapi.cn/Record.List"
    params = {
        'login_token': login_token,
        'format': 'json',
        'domain': domain,
        'sub_domain': sub_domain,
        'record_type': 'A',
        'offset':0,
        'length': 3,
    }
    return REQ(url, params)


@checkResponse
def createRecord(login_token, domain, sub_domain, ip):
    # curl -X POST https://dnsapi.cn/Record.Create -d 'login_token=LOGIN_TOKEN&format=json&domain_id=2317346&sub_domain=@&record_type=A&record_line_id=10%3D0&value=1.1.1.1'
    url = "https://dnsapi.cn/Record.Create"
    params = {
        'login_token': login_token,
        'format': 'json',
        'domain': domain,
        'sub_domain': sub_domain,
        'record_type': 'A',
        'record_line': '默认',
        'value': ip,
    }
    return REQ(url, params)


@checkResponse
def modifyRecord(login_token, domain, sub_domain, record_id, new_ip):
    # curl -X POST https://dnsapi.cn/Record.Modify -d 'login_token=1234,abcd&format=json&domain=yourdomain.com&record_id=842462794&sub_domain=ddns&value=192.168.31.35&record_type=A&record_line_id=10%3D0'
    url = "https://dnsapi.cn/Record.Modify"
    params = {
        'login_token': login_token,
        'format': 'json',
        'domain': domain,
        'sub_domain': sub_domain,
        'record_id': record_id,
        'value': new_ip,
        'record_line': '默认',
    }
    return REQ(url, params)


# 设置成功后会把 TTL 变成 10
@checkResponse
def ddnsRecord(login_token, domain, sub_domain, record_id, new_ip):
    # curl -X POST https://dnsapi.cn/Record.Ddns -d 'login_token=1234,abcd&format=json&domain=yourdomain.com&record_id=842462794&sub_domain=ddns&value=127.0.0.1&record_line_id=10%3D0'
    url = "https://dnsapi.cn/Record.Ddns"
    params = {
        'login_token': login_token,
        'format': 'json',
        'domain': domain,
        'sub_domain': sub_domain,
        'record_id': record_id,
        'value': new_ip,
        'record_line': '默认',
    }
    return REQ(url, params)


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4: return False

    for x in a:
        if not x.isdigit(): return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def getLocalIP():
    res = ''
    import socket
    if platform.system().lower() == 'windows':
        res = socket.gethostbyname(socket.gethostname())
    else:
        sh = "/sbin/ifconfig | /usr/bin/grep 'inet ' | /usr/bin/grep -v 127.0.0.1 | /usr/bin/awk '{print $2}'"
        with os.popen(sh) as f:
            res = f.read()
        res = res.strip()

    return res if validate_ip(res) else ''


def getInetIP():
    url = 'https://httpbin.org/ip'
    res = REQ(url)
    return res['origin']


def checkCrontab(stop=False, minutes=1):
    if platform.system().lower() == 'windows':
        taskname = "MyTasks\\ddns4DNSPod task"
        if os.popen(f'schtasks.exe /QUERY /TN "{taskname}"').read():
            if stop:
                os.popen(f'schtasks.exe /DELETE /F /TN "{taskname}"')
            return

        if stop: return

        # pythonw 不会弹出 command prompt 窗口
        # https://docs.microsoft.com/en-us/previous-versions/orphan-topics/ws.10/cc772785(v=ws.10)?redirectedfrom=MSDN
        sh = f'schtasks.exe /CREATE /SC MINUTE /MO {minutes} /TN "{taskname}" /TR "pythonw {os.path.abspath(__file__)}"'
        with os.popen(sh) as f:
            res = f.read()
            print(res)
        return

    import crontab
    ct = crontab.CronTab(user=True)

    comment = 'crontab_ddns4DNSPod'

    if len(ct.crons) > 0:
        for job in ct:
            if job.comment == comment:
                if stop:
                    ct.remove(job)
                    ct.write()
                return

    if stop: return

    job = ct.new(command=f'/usr/bin/python3 {os.path.abspath(__file__)}', comment=comment)
    job.minute.every(minutes)
    ct.write()


def curtime():
    t = time.time()
    tm = time.gmtime(t) # tm = time.localtime(time.time())
    fmt = '%a, %d %b %Y %H:%M:%S GMT'
    return time.strftime(fmt, tm)

def localstrtime(ts=None):
    return time.strftime('%Y_%b_%d_%a_%H:%M:%S', time.localtime(ts or time.time()))

def mktimefromstr(s):
    m = re.search('.*?(\d.*)\.', s) # timestamp
    try:
        return time.mktime(time.strptime(m.group(1), '%Y_%b_%d_%a_%H:%M:%S'))
    except Exception as e:
        return None
    return None

raw_print = print
def print(*args, **kwargs):
    return raw_print(localstrtime(), *args, **kwargs)

def eprint(*args, **kwargs):
    return raw_print(localstrtime(), *args, file=sys.stderr, **kwargs)


def main():
    # https://www.cnblogs.com/hangj/p/14956420.html # redirect stdout to /dev/null, for the sick of 'You have mail in /var/mail/xxx'
    # sys.stdout = open(os.devnull, 'w')

    # local_ip = getLocalIP()
    inet_ip = getInetIP()

    record_list = getRecordList(login_token, domain, sub_domain)
    if int(record_list['status']['code']) == 10:
        res = createRecord(login_token, domain, sub_domain, inet_ip)
        if int(res['status']['code']) != 1:
            print('createRecord failed: ', res)
            return
        else:
            record_list = getRecordList(login_token, domain, sub_domain)
    
    record = record_list['records'][0]
    record_id, record_ip, ttl = record['id'], record['value'], int(record['ttl'])

    if inet_ip == record_ip:
        return

    res = ddnsRecord(login_token, domain, sub_domain, record_id, inet_ip)

    print(f"{localstrtime()} inet_ip: {inet_ip}")
    print(f"{localstrtime()} record_ip: {record_ip}")
    print(f'{localstrtime()} Ddns: {res}')



if __name__ == '__main__':
    cfd = os.path.dirname(os.path.abspath(__file__)) # current file directory
    basename = os.path.basename(__file__)
    os.chdir(cfd)

    sys.stdout = open(f'./{basename}.log', 'a')
    sys.stderr = open(f'./{basename}.err.log', 'a')

    main()



# 每 5 分钟执行一次
# crontab -e
# */5 * * * * ddns4dnspod.py

# EOF
