from bs4 import BeautifulSoup
import requests
import json

url = 'https://mikrokreditbank.uz/'

list1 = []
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")
divList = soup.find('div', attrs={"class": "convertor-content"})
tr = divList.find_all('td')

i = 0
for wr in tr:
    list1.append(wr.text)


