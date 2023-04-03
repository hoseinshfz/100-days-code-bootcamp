import requests
from bs4 import BeautifulSoup
from notification_manager import NotificationManager

BUY_PRICE = 65.95

URL = "https://www.amazon.nl/ADATA-HD710P-Festplatte-USB-3-1/dp/B0744NCY4K/ref=sr_1_2?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2TX6UWB4VS0J1&keywords=adata%2Bhdd&qid=1680522324&sprefix=adata%2Bhdd%2Caps%2C110&sr=8-2&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


def send_message(title, price):
    messenger = NotificationManager()
    message = f'{title} is now €{price}'
    messenger.send_email(message)
    messenger.telegram_bot_send_text(message)


response = requests.get(url=URL, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

title = soup.find(id="productTitle").get_text().strip()

whole_price = soup.find("span", class_="a-price-whole")
fraction_price = soup.find("span", class_="a-price-fraction")

price = (whole_price.getText() + fraction_price.getText()).replace(',', '.')
price_float = float(price)

if price_float <= BUY_PRICE:
    send_message(title, price)

