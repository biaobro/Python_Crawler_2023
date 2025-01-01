# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : Top250.py
@Project            : Crawler_2022
@CreateTime         : 2022/1/23 11:14
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/1/23 11:14
@Version            : 1.0
@Description        : B站IT私塾
        @重点
        1，正则表达式
        2，写入sqlite3
"""
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

pageLinkPattern = re.compile(r'<a href="(.*?)">')
imgLinkPattern = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 忽略换行符合
titlePattern = re.compile(r'<span class="title">(.*)</span>')
ratingPattern = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
judgePattern = re.compile(r'<span>(\d*)人评价</span>')
inqPattern = re.compile(r'<span class="inq">(.*)</span>')

# 有的电影是 [可播放],有的电影是什么都没有
playablePattern = re.compile(r'<span class="playable">\[(.*?)]</span>')
bdPattern = re.compile(r'<p class="">(.*?)</p>', re.S)


# ? 表示在遇到第0个或第1个 </p>的时候就停下来,否则会一直匹配到最后，即所谓的贪婪模式


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)

    # save into excel
    # savepath = "豆瓣电影Top250.xls"  # ..表示上级目录
    # saveInExcel(savepath, datalist)

    # save into db
    dbpath = "movie.db"
    saveInDB(dbpath, datalist)

    # response = urllib.request.urlopen("https://www.baidu.com")
    # print(response)  # HTTPResponse
    # print(response.read().decode('utf-8'))
    # askURL(baseurl)



def getData(baseurl):
    datalist = []

    # grab the document
    for i in range(10):
        url = baseurl + str(i * 25)
        print(url)
        html = askURL(url)
        # datalist.append(html)

        # retrieve the document
        soup = BeautifulSoup(html, 'html.parser')

        # 找到class 属性为item 的 div标签
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)

            pageLink = re.findall(pageLinkPattern, item)[0]
            data.append(pageLink)

            imgLink = re.findall(imgLinkPattern, item)[0]
            data.append(imgLink)

            titles = re.findall(titlePattern, item)
            if (len(titles)) == 2:
                cTitle = titles[0]
                data.append(cTitle)
                oTitle = titles[1].replace('/', '')
                data.append(oTitle)
            else:
                data.append(titles[0])
                data.append(' ')  # keep empty

            rating = re.findall(ratingPattern, item)[0]
            data.append(rating)

            judge = re.findall(judgePattern, item)[0]
            data.append(judge)

            inq = re.findall(inqPattern, item)
            if len(inq) != 0:
                inq = inq[0].replace('.', '')
                data.append(inq)
            else:
                data.append(' ')

            playable = re.findall(playablePattern, item)
            if len(playable) == 1:
                data.append(playable[0])
            else:
                data.append(' ')

            bd = re.findall(bdPattern, item)[0]
            bd = re.sub(r'<br(\s+)?/>(\s+)?', ' ', bd)  # remove </br>
            bd = re.sub(r'/', ' ', bd)
            data.append(bd.strip())  # remove space

            # print(data)
            datalist.append(data)
        # print(datalist)
    return datalist


def askURL(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 Safari/537.36',
    }
    req = urllib.request.Request(url, headers=header)
    html = ''
    try:
        resp = urllib.request.urlopen(req)
        html = resp.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


def saveInExcel(savepath, datalist):
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    column = ('pageLink', 'imgLink', 'ctitle', 'otitle', 'rating', 'judge', 'inq', 'playable', 'bd')
    for i in range(len(column)):
        worksheet.write(0, i, column[i])

    for i in range(len(datalist)):
        print('write the {}th'.format(i + 1))
        for j in range(len(datalist[i])):
            worksheet.write(i + 1, j, datalist[i][j])

    workbook.save(savepath)


def saveInDB(dbpath, datalist):
    initDB(dbpath)

    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5: continue
            data[index] = '"' + data[index] + '"'
        sqlInsert = '''
                insert into movie (pageLink, imgLink, ctitle, etitle, rating, judge, inq, playable, bd)
                values (%s)
            ''' % ",".join(data)
        print(sqlInsert)
        cursor.execute(sqlInsert)
        conn.commit()
    cursor.close()
    conn.close()
    print("open database successfully")


def initDB(dbpath, name='movie'):
    sqlCreateTable = '''
            create table movie
            (
            id integer primary key autoincrement,
            pageLink text,
            imgLink text,
            ctitle varchar,
            etitle varchar,
            rating numeric,
            judge numeric,
            inq text,
            playable text, 
            bd text
            );
        '''
    conn = sqlite3.connect(dbpath)
    print("open database successfully")

    cursor = conn.cursor()
    cursor.execute(sqlCreateTable)
    conn.commit()
    cursor.close()
    conn.close()

    print("database and table init done.")


if __name__ == '__main__':
    main()
    # data = '"123""456"'
    # sqlInsert = '''
    #                     insert into movie (pageLink, imgLink, ctitle, otitle, rating, judge, inq, playable, bd)
    #                     values (%s)
    #                 ''' % ",".join(data)
    # print(sqlInsert)
