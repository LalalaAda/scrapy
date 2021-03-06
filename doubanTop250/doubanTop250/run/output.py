#!/usr/bin.python
# -*- coding: utf-8 -*-

import json

def readMovieJson():
    with open("items.json", "r") as inFile:
        text = inFile.read()
        movie_dict = json.loads(text)
        for movie in movie_dict:
            rank = movie["rank"][0]
            title = movie["title"][0]
            link = movie["link"][0]
            star = movie["star"][0]
            rate = movie["rate"][0]
            if movie["quote"]:
                quote = movie["quote"][0]
            else:
                quote = u"暂无"
            
            print("top" + rank + "." + \
                title + u" 评分" + star + \
                '(' + rate + ')' + \
                u"\n链接：" + link + \
                u"\n豆瓣评论：" + quote + "\n")

if __name__ == '__main__':
    readMovieJson()
