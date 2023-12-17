
from bs4 import BeautifulSoup
import requests

r=requests.get('https://www.trendyol.com/sr?q=telefon&qt=telefon&st=telefon&os=1')

source=BeautifulSoup(r.content,"lxml")

urls=source.find_all("div",attrs={"class":"p-card-chldrn-cntnr"})

for url in urls:
    url_phone="https://www.trendyol.com/"+url.a.get("href")
    print(url.text)
    print(url_phone)