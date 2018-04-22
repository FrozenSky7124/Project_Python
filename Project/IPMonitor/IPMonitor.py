#!/usr/bin/python
# -*- coding:utf8 -*-

__author__ = 'FrozenSky'

import socket
import fcntl
import time
import struct
import smtplib
import urllib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
import urllib2
import os

# E-Mail Config
smtpserver = "smtp.qq.com"
username = "xxxxxxx@foxmail.com"
password = "xxxxxxx"
sender = "xxxxxxx@foxmail.com"
receiver = ["xxxxxxx@qq.com"]
subject = "[RaspberryPi][IPMonitor]IpAddr"

# File_Path Config
file_path = "/home/pi/Applications/IPMonitor/LastIP"

def sendEmail(msghtml):
    msgRoot = MIMEMultipart('related')
    msgRoot["To"] = ';'.join(receiver)
    msgRoot["From"] = sender
    msgRoot['Subject'] =  subject
    msgText = MIMEText(msghtml,'html','utf-8')
    msgRoot.attach(msgText)
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    #smtp.connect(smtpserver, 465)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

def check_network():
    while True:
        try:
            print "Network is Ready!"
            break
        except Exception , e:
            print e
            print "Network is not ready,Sleep 5s...."
            time.sleep(10)
    return True

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ipaddr=s.getsockname()[0]
    s.close()
    return ipaddr

class Getmyip:
    def getip(self):
        try:
            myip = self.visit("http://ip.chinaz.com/getip.aspx")
        except:
            try:
                myip = self.visit("http://ddns.oray.com/checkip")
            except:
                try:
                    myip = self.visit("http://members.3322.org/dyndns/getip")
                    # if you want to add more,use the format "except try"
                    # make sure the most useful link be the first
                except:
                    print "Fail to get the Network ip."
                    print "Get the LAN ip."
                    myip = get_lan_ip()
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url,timeout=20)
        if url == opener.geturl():
            str = opener.read()
            print "IP information from: ",url
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)

def get_network_ip():
    getmyip = Getmyip()
    localip = getmyip.getip()
    return localip


if __name__ == '__main__':
    check_network()
    ipaddr=get_network_ip()
    lanip=get_lan_ip()
    show_ip="WAN_IP: "+str(ipaddr)+"\n"+"LAN_IP: "+str(lanip)
    ip_file = open(file_path)
    last_ip = ip_file.read()
    ip_file.close()
    if last_ip == show_ip:
        print "IP not change."
    else:
        print "IP changed.\n{}".format(show_ip)
        ip_file = open(file_path,"w")
        ip_file.write(str(show_ip))
        ip_file.close()
        
        # Submit to OrayDDNS
        strCommit = "curl -s http://xxxxxxx:xxxxxxxOray@ddns.oray.com/ph/update?hostname=xxxxxxx&myip="+str(ipaddr)
        webinfo = os.popen(strCommit).read()
        if 'good' in webinfo:
            print "Successfully commit to OrayDDNS."
            emailip="<font face=\"Courier New\" size=\"3\">WAN_IP: "+str(ipaddr)+"<br>"+"LAN_IP: "+str(lanip)+"<br>"+"Successfully commit to OrayDDNS.</font>"
        else:
            print "Failed to commit to OrayDDNS."
            emailip="<font face=\"Courier New\" size=\"3\">WAN_IP: "+str(ipaddr)+"<br>"+"LAN_IP: "+str(lanip)+"<br>"+"Failed to commit to OrayDDNS.</font>"
        
        # Send the E-Mail
        sendEmail(emailip)