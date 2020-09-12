# http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/

import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c,"html.parser")

all  = soup.find_all("div",{"class":"property-card"})

all[0].find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")


l = []
for item in all:
    d = {}
    d["Price"]=item.find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")
    d["Address"]=item.find_all("div",{"class":"property-address"})[0].text.replace("\n","").lstrip()
    d["City"]=item.find_all("div",{"class":"property-city"})[0].text.replace("\n","").lstrip()
    d["Beds"]=item.find_all("div",{"class":"property-beds"})[0].find("strong").text
    d["Baths"]=item.find_all("div",{"class":"property-baths"})[0].find("strong").text
    try:
       d["Half-Baths"]=item.find_all("div",{"class":"property-half-baths"})[0].find("strong").text
    except:
        d["Half-Baths"]=None
    try:
        d["Area(Sq.ft)"]=item.find_all("div",{"class":"property-sqft"})[0].find("strong").text
    except:
        d["Area(Sq.ft)"]=None
    print(" ")
    l.append(d)

df = pandas.DataFrame(l)

df.to_csv("realdata.csv")