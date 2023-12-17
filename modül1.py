from urllib import request
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

#Gerekli Listeler
url_list=[]
prices_list=[]
propTitles=[]
propValues=[]

#Degerlerin cekilmesi
for i in range(1,30) # gidilecek sayfa sayisi
url="https://www.trendyol.com/sr?q=cep%20telefonu&qt=cep%20telefonu&st=cep%20telefonu&os="+str(i)
r=requests.get(url) #elde edilen url'ye baglanma istegi
source=BeautifulSoup(r.content,"lxml")#verilerin cekilme islemi

urls=source.find_all("div",attrs={"p-card-clhdrn-cntnr.card-border"})
for url in urls
url_phone="https://www.trendyol.com/"+url.a.get("href")
url_list.append(url_phone)#linkler listeye kaydediliyor
print(url_phone)

r_phone=requests.get(url_phone) #linke istek atiliyor
source_phone=BeautifulSoup(r_phone.content,"lxml")#lxml formatinda veri cekiliyor

properties=source_phone.find_all("li",attrs={"class":"attribute-item"})
for prop in properties:
    prop_title=prop.find("span",attrs={"class":"attribute-label"}).text
    prop_value=prop.find("span",attrs={"class":"attribute-value"}).text
    propTitles.append(prop_title)
    propValues.append(prop_value)
    
prices=source.find_all("span",attrs={"class":"prc-dsc"})
for price in prices:
    prices_list.append(price.text)
    print(price.text)
    
print(str(len(url_list))+"adet link bulundu.")
print(str(len(prices_list))+"adet fiyat bulundu.")
print(str(len(propTitles))+"adet ozellik basligi bulundu.")
print(str(len(propValues))+"adet ozellik verisi bulundu.")

#url ve fiyatlari dataframe'e aktarma
df_urls=pd.DataFrame()
df_urls["urls"]=url_list
df_urls["prices"]=prices_list

df_urls.head()

#bulunan veri sayisi
phones=len(url_list)

#bulunan ozellik basliklarinin benzersizini bulma
columns=np.array(propTitles)
columns=np.unique(columns)

#url ve fiyat bilgilerini iceren yeni dataframe
df=pd.DataFrame(columns=columns)
df["url"]=url_list
df["price"]=prices_list

#yeni dataframe'nin gosterimi
df.head()

#dataframe kullanarak verileri cekme ve sutuna yazdirma islemi
for i in range(0,phones):
    url=df['url'].loc[i]
    r=requests.get(url)
    source=BeautifulSoup(r.content,"lxml")
    
properties=source.find_all("li",attrs={"class":"attribute-item"})
for prop in properties:
    prop_title=prop.find("span",attrs={"class":"attribute-label"}).text
    prop_value=prop.find("span",attrs={"class":"attribute-value"}).text
    print(prop_title+prop_value)
    df[prop_title].loc[i]=prop_value
    
df.head()

#.csv uzantili dosya haline getirme islemi
df.to_csv("./data/phone_data.csv",index=False)
