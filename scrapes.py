import pandas as pd
from bs4 import BeautifulSoup
import requests
f = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(f.text)
print(soup.get_text())
for i in soup.findAll("div",{"class":"quote"}):
    print((i.find("span",{"class":"text"})).text)