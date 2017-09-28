#中国大学排名定向爬虫



import requests
from bs4 import BeautifulSoup
import bs4
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text = r.text
        return text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = "{0:^5}\t{1:{3}^20}\t{2:^20}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    upai = []
    for i in range(num):
        u = ulist[i]
        u[0] = i+1
        print(tplt.format(u[0], u[1] ,u[2], chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHtmlText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


if __name__ == '__main__':
    main()
