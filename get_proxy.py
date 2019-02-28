#coding=utf-8
import urllib2,urllib
from lxml import etree

url='http://31f.cn/'

def get_page(url):
    page=urllib2.urlopen(url).read().decode('utf-8').encode('utf-8')
    return page

def get_proxy(page):
    data=etree.HTML(page)
    ips=data.xpath('/html/body/div/table[contains(@class,"table") and contains(@class,"table-striped"]/tbody/tr/td')
    ip=[]
    for i in range(len(ips)):
        host=''
        port=''
        if i%3==2:
            host=ips[i]
        elif i%3==0:
            port=ips[i]
        else:
            pass
        ip.append((host,port))
    return ips




print get_proxy(get_page(url))

