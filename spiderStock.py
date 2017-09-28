#股票数据的定向爬虫


import requests
from bs4 import BeautifulSoup
import re
import traceback


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def getStockList(lst, stockURL):
    html = getHtmlText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][zh]\d{6}", href)[0])
        except:
            continue

def getStockinfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHtmlText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            stockName = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({"StockName" : stockName.text.split()[0]})

            keyList = soup.find_all('dt')
            valueList = soup.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前进度： {:.2f}%'.format(count*100/len(lst)), end='')
        except:
            count = count + 1
            print('\r当前进度： {:.2f}%'.format(count * 100 / len(lst)), end='')
            traceback.print_exc()
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://baiduStockInfo.txt'
    sList = []
    getStockList(sList, stock_list_url)
    getStockinfo(sList, stock_info_url, output_file)

if __name__ == '__main__':
    main()
