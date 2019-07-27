#!python3
#-*-coding:utf-8-*-

import urllib,urllib.request,time
from lxml import etree

class GetProxy:
    def __init__(self):
        self.UA = 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en) AppleWebKit/522.15.5 (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5'
        pass

    def sendReauest(self,url = 'https://www.kuaidaili.com/free/intr/'):
        header = {'User-Agent':self.UA}
        req = urllib.request.Request(url,headers = header)
        res = urllib.request.urlopen(req)
        return res.read()

    def htmlParse(self,html):
        #html = self.sendReauest()
        data = etree.HTML(html.decode('utf-8'))        #/html/body/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]
        i = j = 0
        proxyList = []
        for i in range(15):
            tmp = []
            for j in range(7):
                xpathStr = '/html/body/div/div[4]/div[2]/div/div[2]/table/tbody/tr['+str(i+1)+']/td['+str(j+1)+']/child::text()'
                d = data.xpath(xpathStr)
                tmp.append(d[0])
            proxyList.append(tmp)
        with open('proxy.txt','ab') as f:
            for l in proxyList:
                f.write(bytes(' , '.join(l)+'\n',encoding='utf-8'))
        print(proxyList)

    def run(self,baseUrl = 'https://www.kuaidaili.com/free/intr/',n = 20):
        for i in range(n):
            url = baseUrl + str(n + 1)
            html = self.sendReauest(url)
            self.htmlParse(html)
            time.sleep(1)




if __name__  ==  "__main__":
    app = GetProxy()
    app.run()
    