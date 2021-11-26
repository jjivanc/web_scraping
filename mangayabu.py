from bs4 import BeautifulSoup
import requests
#https://appsite.jjivanc.repl.co/
#https://blog.betrybe.com/python/python-list/
headers = {
    'User-Agent':
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}
url = requests.get('https://mangayabu.top/', headers=headers)


def getPage():

	resultado = []

	soup = BeautifulSoup(url.content, 'html.parser')
	searchDiv = soup.find_all('div', class_='mango-hover', limit=18)
	#searchcont = searchDiv.find_all('a')
	for result in searchDiv:
		images = result.find_all('img')
		#print(images)

		resultado.append(images)

	#resultado.append(tabelas)
	return resultado


def getTitulos():
	resultados = []
	soup = BeautifulSoup(url.content, 'html.parser')
	#titulo = soup.find_all("div", class_="card-content", limit=18)
	for title in soup.find_all("div", class_="card", limit=18):
		images = title.select_one('img')['src']
		tabela = title.find_all('h4')[0].get_text()
		print(title)
		resultados.append({"Titulo":'%s'%tabela, "Link":'%s'%images})
	return resultados


if __name__ == "__main__":
	print('foi')
	getPage()
	getTitulos()

	print(getTitulos())
