from bs4 import BeautifulSoup
import requests

url_1 = "https://www.ncei.noaa.gov/data/oceans/ghrsst/L4/GLOB/JPL/MUR25/2002/"
ext = ".nc"
info_pag = requests.get(url_1).text
soup = BeautifulSoup(info_pag, "html.parser")

k = soup.find_all("a")
url_2 = k[5]["href"]
url = [url_1 + "/" + url_2]

print(url)