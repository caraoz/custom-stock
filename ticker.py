import requests
from bs4 import BeautifulSoup

r = requests.get('http://finviz.com/screener.ashx?v=512&f=idx_sp500&o=ticker')
soup = BeautifulSoup(r.content)

for element in soup.findAll(class_='tab-link'):
	print(element.text)