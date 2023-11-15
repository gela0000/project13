import requests 
from bs4 import BeautifulSoup


def main():
	url = "https://www.imdb.com/chart/top"
	header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
	response = requests.get(url, headers=header)
	print(response)

	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all("div", {"class": "sc-c7e5f54-7 brlapf cli-title-metadata"})

	d={}
	for tag in tags:
		info = tag.text
		year = info[0:4]
		if year not in d:
			d[year] = 1
		else:
			d[year] += 1

	for key, value in sorted(d.items(), key=lambda element: element[1]):
		print(key, '-->', value)




if __name__ == '__main__':
	main()
