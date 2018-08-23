import os
import json
import urllib.request
import wget

# アイドルリスト
idol = ["", "Haruka", "Chihaya", "Miki", "Yukiho", "Yayoi", "Makoto",
"Iori", "Takane", "Ritsuko", "Azusa", "Ami", "Mami", "Hibiki", "Mirai",
"Shizuka", "Tsubasa", "Kotoha", "Elena", "Minako", "Megumi", "Matsuri",
"Serika", "Akane", "Anna", "Roco", "Yuriko", "Sayoko", "Arisa", "Umi",
"Iku", "Tomoka", "Emily", "Shiho", "Ayumu", "Hinata", "Kana", "Nao",
"Chizuru", "Konomi", "Tamaki", "Fuka", "Miya", "Noriko", "Mizuki",
"Karen", "Rio", "Subaru", "Reika", "Momoko", "Julia", "Tsumugi", "Kaori"]

# ガシャSSR一覧取得
#url = "https://api.matsurihi.me/mltd/v1/cards?rarity=ssr&extraType=none&prettyPrint=false"
# ガシャSR一覧取得
url = "https://api.matsurihi.me/mltd/v1/cards?rarity=sr&extraType=none&prettyPrint=false"
req = urllib.request.Request(url)
con = urllib.request.urlopen(req)
cards = json.loads(con.read().decode('utf-8'))

# カードダウンロード
for card in cards:
    folder = "./{}/".format(idol[card["idolId"]])
    if os.path.exists(folder) == False:
        os.mkdir(folder)
    for style in ("0", "1"):
        filename = "{}_{}_b.png".format(card["resourceId"], style)
        url = "https://storage.matsurihi.me/mltd/card/{}".format(filename)
        print(filename)
        wget.download(url, out=folder+filename)
        print()