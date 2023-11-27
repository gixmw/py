import requests

from bs4 import BeautifulSoup

headers = {"user-agent": "seoul sangilmedia"}

webpage = requests.get("https://entertain.naver.com/read?oid=311&aid=0001664261&cid=1073789", headers=headers)

soup = BeautifulSoup(webpage.content,"html.parser")

naver_news = soup.select_one("#articeBody").get_text().strip()

print(naver_news)