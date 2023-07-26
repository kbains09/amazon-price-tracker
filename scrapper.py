import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ca/GLASHOM-Standing-Hanging-Leaning-Arched-Top/dp/B0BYK7S6PM/ref=sr_1_5?keywords=wall%2Bmirror%2Bfull%2Blength&qid=1690353934&sprefix=wall%2Bmirror%2Caps%2C242&sr=8-5&ufe=app_do%3Aamzn1.fos.d0e27fc4-6417-4b26-97cb-f959a9930752&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[5:]) #the first 5 characters are the currency symbol

print(converted_price) 
print(title.strip())
