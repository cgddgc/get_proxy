#coding=utf-8
import urllib2,urllib,sys,json,random,ssl,time
from lxml import etree
reload(sys)
sys.setdefaultencoding( "utf-8" )
ssl._create_default_https_context = ssl._create_unverified_context

agents=[
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
        ]

url='http://31f.cn/'
url1="https://www.kuaidaili.com/free/intr/2"

def get_page(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0','Host':'www.kuaidaili.com'}
    #proxy_handler=urllib2.ProxyHandler({'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'})
    #opener=urllib2.build_opener(proxy_handler)
    #urllib2.install_opener(opener)
    req=urllib2.Request(url,headers=header)
    #req.add_header(header)
    page=urllib2.urlopen(req).read().decode('utf-8').encode('utf-8')
    #print page
    return page

def write(name,data):
    #try:
    f=open(name,'a+')
    for i in data:
        f.write(','.join(i))
        f.write('\n')
    #finally:
    f.close()

def get_proxy(url):
    page=get_page(url)
    data=etree.HTML(page.encode('utf-8'))
    ips=data.xpath('/html/body/div[@class="body"]/div[@id="content"]/div[@class="con-body"]/div/div[@id="list"]/table/tbody/tr/td/child::text()')#
    ip=[]
    for i in range(0,len(ips)-1):
        if i%7==0:
            #unit={'method':ips[i+3],'host':ips[i],'port':ips[i+1]}
            unit=[ips[i],ips[i+1],ips[i+3],ips[i+4]]
            ip.append(unit)
            #print ips[i].encode('utf-8').decode('utf-8')
        else:
            pass
    #print ip
    proxys=[]
    for i in ip:
        if i[2]=='HTTP':
            tmp='http://'+i[0]+':'+str(i[1])
        elif i[2]=='HTTPS':
            tmp='https://'+i[0]+':'+str(i[1])
        else:
            tmp=''
        proxys.append(tmp)
    #print proxys
    return proxys

def safe_proxy(n):
    for i in range(n):
        url="https://www.kuaidaili.com/free/inha/"+str(i+1)
        #print url
        fname='proxy.txt'
        write(fname,get_proxy(url))
        time.sleep(1)




#get_proxy(url1)
def test():
    proxy_handler=urllib2.ProxyHandler({'http':random.choice(get_proxy(url1))})
    opener=urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    p=urllib2.urlopen('http://myip.kkcha.com/').read()
    data=etree.HTML(p.encode('utf-8'))
    ip=data.xpath('/html/body/div[contains(@class,"pm") and contains(@class,"home")]/div/div/child::text()')
    print ip[0]

#test()
#print 
#get_proxy(get_page(url1))
#write('proxys.txt',get_proxy(get_page(url1)))
#safe_proxy(5)
