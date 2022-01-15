

BaseConfig = {
    'menuList':'#list a',
    'bookName':'',
    'chartTile':'.bookname h1',
    'chartContent':'#content',
}

Config = {
    'http://www.biquge001.com/':BaseConfig,
    'https://www.xbiquge.la/':BaseConfig,
    'http://www.ibiqu.net/':BaseConfig,
    'https://www.biquge.biz/':BaseConfig,
    'https://www.biqugee.com/':BaseConfig,
}

print(Config['https://www.biqugee.com/'])