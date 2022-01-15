# http://www.26ksw.cc/book/10258/

# coding:utf-8
# import urllib
# import urllib.request
import requests
from bs4 import BeautifulSoup
import multiprocessing
import re
import os
import time

from utils import removeN, trim


# 通过章节的url下载内容，并返回下一页的url
def get_ChartTxt(url,title,num,totalNum):
    print('本章节地址： ' + url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    res = requests.get(url, headers=headers)  # get方法中加入请求头
    # 查看下当前requests请求url抓去的数据编码,这里获取的是ISO-8859-1
    # print("原址编码：%s" % (requests.get(url).encoding))
    # 翻阅下要爬去的网站的编码是什么，这里看了下是utf-8，编码不一样会乱码，将requests获取的数据编码改为和目标网站相同，改为utf-8
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')  # 对返回的结果进行解析

    # 查找章节名
    # <div class="bookname">
    #             <h1>第1章 大康王朝</h1>
    #             ...
    # </div>
    chartTile = soup.select('.bookname h1')[0].get_text()
    # [<h1>第1章 大康王朝</h1>]

    print('正在下载 (%d/%d) %s %s' % (num,totalNum,chartTile,url))

    return


    # <meta property="og:novel:book_name" content="天命王侯">
    # meta property="og:novel:book_name" content="(.*?)"
    title = soup.find(attrs={"property": "og:novel:book_name"})['content']

    print('正在下载 《%s》' % (title))

    # 开始计时
    start = time.time()

    return


    soup=get_pages(url)

    # 获取章节名称
    subtitle = soup.select('#htmltimu')[0].text
    # 判断是否有感言
    if re.search(r'.*?章', subtitle) is  None:
        return
    # 获取章节文本
    content = soup.select('#htmlContent')[0].text
    # 按照指定格式替换章节内容，运用正则表达式
    content = re.sub(r'\(.*?\)', '', content)
    content = re.sub(r'\r\n', '', content)
    content = re.sub(r'\n+', '\n', content)
    content = re.sub(r'<.*?>+', '', content)


    # 单独写入这一章
    try:
        with open(r'.\%s\%s %s.txt' % (title, num,subtitle), 'w', encoding='utf-8') as f:
            f.write(subtitle + content)
        f.close()
        print(num,subtitle, '下载成功')

    except Exception as e:
        print(subtitle, '下载失败',url)
        errorPath='.\Error\%s'%(title)
        # 创建错误文件夹
        try :
            os.makedirs(errorPath)
        except Exception as e:
            pass
        #写入错误文件
        with open("%s\error_url.txt"%(errorPath),'a',encoding='utf-8') as f:
            f.write(subtitle+"下载失败 "+url+'\n')
        f.close()
    return

# 通过首页获得该小说的所有章节链接后下载这本书
def thread_getOneBook(url):
    print('小说首页地址： ' + url)

    # url = 'http://www.cnplugins.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    res = requests.get(url, headers=headers)  # get方法中加入请求头
    # 查看下当前requests请求url抓去的数据编码,这里获取的是ISO-8859-1
    print("原址编码：%s" % (requests.get(url).encoding))
    # 翻阅下要爬去的网站的编码是什么，这里看了下是utf-8，编码不一样会乱码，将requests获取的数据编码改为和目标网站相同，改为utf-8
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')  # 对返回的结果进行解析

    # 查找小书名
    # <meta property="og:novel:book_name" content="天命王侯">
    # meta property="og:novel:book_name" content="(.*?)"
    title = soup.find(attrs={"property": "og:novel:book_name"})['content']

    print('正在下载 《%s》' % (title))

    # 开始计时
    start = time.time()

    # 根据书名创建文件夹
    if title not in os.listdir('.'):
        os.mkdir(r".\%s" % (title))
        print(title, "文件夹创建成功")

    # 获取这本书的所有章节
    charts_url = []
    url_chartTitle = dict()
    # 提取出书的每章节不变的url
    regular = re.compile(r'[http|https]+://[^\s]*[.com|.cn|.cc]/')
    baseUrl = re.findall(regular, url)[0]

    print('顶级域名：%s' % (baseUrl))

    index = 0

    # print (soup.select('body > section > div.wrapbox > div:nth-child(1) > div > ul > li:nth-child(6)'))
    # nth-child 在python中运行会报错，需改为 nth-of-type
    # print (soup.select('body > section > div.wrapbox > div:nth-of-type(1) > div > ul > li:nth-of-type(6)'))
    textlist = soup.select('#list.clearfix a')
    for t in textlist:
        # print(type(t))
        # <a href="/book/10258/53450024.html">
        #             第475章 五百人足矣
        #         </a>
        # print (t) #获取单条html信息
        chart_title = trim(removeN(t.get_text()))
        chart_url = t['href']

        url_chartTitle[chart_url] = chart_title

        if chart_url in charts_url:
            charts_url.remove(chart_url) # 移除之前已有的重复项
            charts_url.append(chart_url)
        else:
            index += 1
            charts_url.append(chart_url)            

        # print('%d %s %s' % (index, chart_title, chart_url))  # 获取中间文字信息

    totalNum = len(charts_url)
    print('总共找到 %d 章' % (totalNum))
    # print(url_chartTitle)

    # 创建下载这本书的进程
    p = multiprocessing.Pool()
    # 自己在下载的文件前加上编号，防止有的文章有上，中，下三卷导致有3个第一章
    num=1
    for i in charts_url:
        if (baseUrl.endswith('/') and i.startswith('/')):
            baseUrl = baseUrl.rstrip('/')
        
        url = baseUrl+i
        p.apply_async(get_ChartTxt, args=(url,title,num,totalNum))
        num+=1
        # break

    print('等待 %s 所有的章节被加载......' % (title))
    p.close()
    p.join()
    end = time.time()
    print('下载 %s  完成，运行时间  %0.2f s.' % (title, (end - start)))
    print('开始生成 %s ................' %title )
    # sort_allCharts(r'.',"%s.txt"%title)
    return

# 创建下载多本书书的进程


def process_getAllBook(urls):
    # 输入你要下载的书的首页地址
    print('主程序的PID：%s' % os.getpid())

    print("-------------------开始下载-------------------")
    p = []
    for i in urls:
        p.append(multiprocessing.Process(target=thread_getOneBook, args=(i,)))
    print("等待所有的主进程加载完成........")
    for i in p:
        i.start()
    for i in p:
        i.join()
    print("-------------------全部下载完成-------------------")

    return


urls = [
    'http://www.26ksw.cc/book/10258/'
]

if __name__ == "__main__":
    # 下载指定的书
    process_getAllBook(urls)  # 如果下载完出现卡的话，请单独执行如下命令
    # sort_allCharts(r'.\龙血战神',"龙血战神.txt")
