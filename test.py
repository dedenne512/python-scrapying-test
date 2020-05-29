import urllib.request
from bs4 import BeautifulSoup

url = "https://wiki.ポケモン.com/wiki/%E3%83%95%E3%82%B7%E3%82%AE%E3%83%80%E3%83%8D"
data = None
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


# 日本語ドメインのエラー対策
req = urllib.request.Request(url)
req.add_header('Host', req.host.encode('idna'))

# サイトのHTMLリソースを取得する
res = urllib.request.urlopen(req)
html = res.read()

# print(html)

soup = BeautifulSoup(html, "html.parser")
tag = soup.select("#mw-content-text > div:nth-child(1) > dl:nth-child(13) > dd:nth-child(2)")

print(tag.string)