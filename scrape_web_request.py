# import pandas as pd
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
soup = BeautifulSoup(html_text.text,"lxml")
jobs = soup.find('li', class_='clearfix job-bx wht-shd-bx')
print(jobs)