import requests
import gzip
import bs4

headers = {"Accept": r"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": r"utf-8",
"User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
res = requests.get("https://movie.douban.com/chart", headers=headers)

#contentHtml = gzip.decompress(res.content)
contentHtml = res.text
statusCode = res.status_code

#print(contentHtml)
#print(statusCode)

soup = bs4.BeautifulSoup(contentHtml, "html.parser")
targets = soup.find_all("div", class_ = "pl2")

f = open("a.html", "w", encoding="utf-8")

for each in targets:
	name = each.a.text.split("\n")[1].strip()
	url = each.a["href"]
	print(name)
	print(url)
	f.write("%s ---url= %s \n"%(name, url))

f.close()