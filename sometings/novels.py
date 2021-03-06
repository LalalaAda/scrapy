# -*- coding:UTF-8 -*-
from typing import Text
from bs4 import BeautifulSoup
import requests, re, sys


# pattern_catalog = re.compile(r'<dt>.*(\r|\n|\s)*</dt>')
# pattern_body = re.compile(r'\(https://.*(\r|\n|\s)*.*m\.23xsww\.com')

# if __name__ == '__main__':
#     target = 'https://www.23xsww.com/book/25030/25030968/101949525.html'
#     req = requests.get(url=target)
#     html = req.text
#     bf = BeautifulSoup(html, features="html.parser")
#     texts = bf.find_all('div', class_ = 'showtxt')
#     txt = texts[0].text.replace('\xa0'*8, '\n\n')
#     reallyTxt = pattern_body.sub('\t', txt)
#     print(reallyTxt)

# if __name__ == '__main__':
#     server = 'https://www.23xsww.com/'
#     target = 'https://www.23xsww.com/book/25030/25030968/'
#     req = requests.get(url=target)
#     html = req.text
#     div_bf = BeautifulSoup(html, features="html.parser")
#     div = div_bf.find_all('div', class_='listmain')
#     a_bf = BeautifulSoup(str(div[0]), features="html.parser")
#     dd = pattern_catalog.split(str(a_bf.dl))[4].replace('\n</dl>','')
#     dd_a_bf = BeautifulSoup(dd, 'html.parser')
#     a = dd_a_bf.find_all('a')
#     for each in a:
#         print(each.string, server + each.get('href'))

class downloader(object):
    pattern_catalog = re.compile(r'<dt>.*(\r|\n|\s)*</dt>')
    # 去除尾部 以m.23xsww.com结尾的文本 例如 全本精彩小说尽在m.23xsww.com
    # pattern_body = re.compile(r'\(https://.*(\r|\n|\s)*.*m\.23xsww\.com')
    pattern_body = re.compile(r'请记住本书首发域名：www.cc148.com笔趣阁手机版阅读网址：m.cc148.com')
    clear_re = re.compile(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020|\t|\r')

    def __init__(self):
        # self.server = 'https://www.23xsww.com/'
        self.server = 'https://www.cc148.com/'
        # self.target = 'https://www.23xsww.com/book/25030/25030968/'
        self.target = 'https://www.cc148.com/43_43648/'
        self.names = []     #存放章节名
        self.urls = []      #存放章节链接
        self.nums = 0       #章节数
        self.bookName = '绝地求生捡碎片000'
        self.reqEncoding = 'gbk' # request请求时有些网站中文乱码 可以设置请求编码
    
    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = self.reqEncoding
        html = req.text
        div_bf = BeautifulSoup(html, 'html.parser')
        # div = div_bf.find_all('div', class_='listmain')
        div = div_bf.find_all('div', id='list')
        a_bf = BeautifulSoup(str(div[0]), 'html.parser')
        dd = self.pattern_catalog.split(str(a_bf.dl))[4].replace(r'\n</dl>','')
        dd_a_bf = BeautifulSoup(dd, 'html.parser')
        a = dd_a_bf.find_all('a')
        self.nums = len(a)
        for item in a:
            self.names.append(item.string)
            # self.urls.append(self.server + item.get('href'))
            self.urls.append(self.target + item.get('href'))

    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = self.reqEncoding
        html = req.text
        bf = BeautifulSoup(html, features="html.parser")
        texts = bf.find_all('div', id = 'content')
        txt = texts[0].text
        txt = self.clear_re.sub('\n', txt)
        txt = self.pattern_body.sub('', txt)
        return txt

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('<<小说小说>>开始下载：')
    # print(dl.urls)
    for i in range(dl.nums):
        dl.writer(dl.names[i], dl.bookName+".txt", dl.get_contents(dl.urls[i]))
        sys.stdout.write(" 已下载：%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('<<小说小说>>下载完成')
