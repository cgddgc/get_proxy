#!python3
#-*-coding:utf-8-*-

import urllib,urllib.request,lxml

class GetProxy:
    def __init__(self):
        self.UA='Mozilla/5.0 (Windows; U; Windows NT 6.0; en) AppleWebKit/522.15.5 (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5'
        pass

    def sendReauest(self,url='https://www.kuaidaili.com/free/intr/'):
        header={'User-Agent':self.UA}
        req=urllib.request.Request(url,headers=header)
        res=urllib.request.urlopen(req)
        return res.read()

    def htmlParse(self,html):
        data=etree.HTML(html.encode('utf-8'))        #/html/body/div/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]










if __name__ == "__main__":
    gp=GetProxy()
    gp.sendReauest()
    