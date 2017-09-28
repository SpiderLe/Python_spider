#网络图片的爬取和存储

import requests
import os

url = 'http://imgsrc.baidu.com/imgad/pic/item/9c16fdfaaf51f3de8c90c3769eeef01f3a297985.jpg'
root = "D://pics//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
        print(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功！")
    else:
        print("文件已存在！")
except:
    print("爬取失败！")
