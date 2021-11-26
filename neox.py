from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


#browser = webdriver.Firefox(options=options)


#browser = webdriver.Firefox(options=options

def pegarneox():
	options = Options()
	options.headless = True
	browser = webdriver.Firefox(options=options)
	browser.get('https://neoxscans.net/')
	page_source = browser.page_source
	soup = BeautifulSoup(page_source, 'html.parser')
	pageList = soup.find_all('div', class_='col-6 col-md-3 badge-pos-2')
	lista = [{}]
	for res in pageList:
		lista.append(res.select_one("img")["data-src"])
	print(f"\nFound total shoes: {len(pageList)}")
		#print(pageList)
		#print(links)
		#print(lista)
	browser.quit()
	return lista


if __name__ == '__main__':
	pegarneox()