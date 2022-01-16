
Host = r'([http|https]+://[^\s]*[.com|.cn|.la|.net|.biz]/)'
OutputDir = 'books'

BaseConfig = {
    'menuList':'#list a', # 章节目录css选择器
    'menuUrlIsFull':False, # 目录页各章节url是否是全路径，不是则按照根域名相对路径
    'bookName':'', # 留空时 小说名从 meta 标签获取 <meta property="og:novel:book_name" content="天命王侯"> ，否则 在此天上 小说名的 css 选择器
    'chapterTile':'.bookname h1', # 章节页章节标题
    'chapterContent':'#content', # 章节页章节内容
}

Config = {
    'http://www.biquge001.com/':BaseConfig,
    'https://www.xbiquge.la/':BaseConfig,
    'http://www.ibiqu.net/':BaseConfig,
    'https://www.biquge.biz/':BaseConfig,
    'https://www.biqugee.com/':BaseConfig,
    'https://biquge96.com/':{
        'menuList':'.mb20 .info-chapters a',
        'bookName':'',
        'chapterTile':'.reader-main h1',
        'chapterContent':'#article',
    },
    # 'http://www.26ksw.cc/':{
    #     'menuList':'#list a',
    #     'bookName':'',
    #     'chapterTile':'.reader-main h1',
    #     'chapterContent':'#article',
    # },
    'http://www.b5200.net/':{
        'menuList':'#list a',
        'menuUrlIsFull':True,
        'bookName':'',
        'chapterTile':'.bookname h1',
        'chapterContent':'#content',
    },
    'https://www.bige7.com/':{
        'menuList':'.listmain a',
        'menuUrlIsFull':False,
        'bookName':'',
        'chapterTile':'.content h1',
        'chapterContent':'#chaptercontent',
    },
    'http://www.soduso.cc/':{
        'menuList':'.ml_list a',
        'menuUrlIsFull':False,
        'bookName':'.introduce h1', # 小说名css选择器
        'chapterTile':'.nr_title h3',
        'chapterContent':'#articlecontent',
    },
}

# print(Config['https://www.biqugee.com/'])
