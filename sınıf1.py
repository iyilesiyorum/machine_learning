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

# Deðerlerin çekilmesi
for i in range(1, 30):  # gidilecek sayfa sayisi
    url = "https://www.trendyol.com/sr?q=telefon&qt=telefon&st=telefon&os=" + str(i)
    r = requests.get(url)  # elde edilen url'ye baðlanma isteði
    source = BeautifulSoup(r.content, "lxml")  # verilerin çekilme iþlemi

    urls = source.find_all("div", attrs={"p-card-chldrn-cntnr"})
    for url in urls:
        url_phone = "https://www.trendyol.com/" + url.a.get("href")
        url_list.append(url_phone)  # linkler listeye kaydediliyor
        print(url_phone)

        # Bu kýsým döngü içinde olmalý, aksi halde en son url_phone deðeri kullanýlýr
        r_phone = requests.get(url_phone)  # linke istek atiliyor
        source_phone = BeautifulSoup(r_phone.content, "lxml")  # lxml formatinda veri cekiliyor
        
        prices = source_phone.find("span", attrs={"class": "prc-dsc"})
        for price in prices:
            prices_list.append(price.text)
            print(price.text)

        
        properties = source_phone.find_all("li", attrs={"class": "attribute-item"})
        for prop in properties:
            prop_title = prop.find("span", attrs={"class": "attribute-label"}).text
            prop_value = prop.find("span", attrs={"class": "attribute-value"}).text
            propTitles.append(prop_title)
            propValues.append(prop_value)

      

print(str(len(url_list)) + " adet link bulundu.")
print(str(len(prices_list)) + " adet fiyat bulundu.")
print(str(len(propTitles)) + " adet ozellik basligi bulundu.")
print(str(len(propValues)) + " adet ozellik verisi bulundu.")

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

for i in range(0, len(df)):
    url = df['url'].loc[i]
    r = requests.get(url)
    source = BeautifulSoup(r.content, "lxml")

    properties = source.find_all("li", attrs={"class": "attribute-item"})
    for prop in properties:
        prop_title = prop.find("span", attrs={"class": "attribute-label"}).text
        prop_value = prop.find("span", attrs={"class": "attribute-value"}).text

        # Her bir özelliði DataFrame'e ekleyin
        df.loc[i, prop_title] = prop_value
        
df.head()

# CSV dosyasýna yazma
df.to_csv(r"C:\Users\hakan\source\repos\machine_learning\phone_data.csv", index=False, encoding="utf-8")