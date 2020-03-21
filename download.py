# 1つ目の引数->検索ワード(複数指定時は"でくくる)
# 2つ目の引数->保存先フォルダー名(自動生成あり)

import sys
import os
from urllib.parse import urlparse
import urllib.request
from bs4 import BeautifulSoup
import wget

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

# 検索文字列
search = sys.argv[1]
# 保存先
save = "./" + sys.argv[2] + "/"
if os.path.exists(save) == False:
    os.mkdir(save)

no = 1
while True:
    print("ページ番号:{}".format(no))
    # URLにアクセスする
    url = "https://mill.tokyo/?page={}&keyword={}".format(no, search)
    p = urlparse(url)
    query = urllib.parse.quote_plus(p.query, safe='=&')
    url = '{}://{}{}{}{}{}{}{}{}'.format(
        p.scheme, p.netloc, p.path,
        ';' if p.params else '', p.params,
        '?' if p.query else '', query,
        '#' if p.fragment else '', p.fragment)
    print(url)
    req = urllib.request.Request(url, headers={'User-Agent' : UA})
    try:
        con = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        break 
    # list取得
    soup = BeautifulSoup(con, "html.parser")
    cardid = soup.findAll('div',{'class':'archive__cardItem__id'})
    if len(cardid) < 1:
        break
    for card in cardid:
        print(card.text)
        if int(card.text) % 100 == 0:
            cardno = '{0:02d}'.format(int(card.text) // 100)
        else:
            cardno = '{0:02d}'.format(int(card.text) // 100 + 1)
        download_url = "https://mill.tokyo/card/noframe{}/noframe{}.jpg".format(cardno, card.text)
        try:
            wget.download(download_url, save + download_url.split('/')[-1])
        except urllib.error.HTTPError:
            download_url = download_url.replace("noframe","frame")
            try:
                wget.download(download_url, save + download_url.split('/')[-1])
            except urllib.error.HTTPError:
                continue
        print()
    no += 1

print("取得完了")