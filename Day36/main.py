import requests
from telegram_messenger import telegram_bot_send_text

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_api = "***"
price_api = "***"

FROM = "2023-03-01"
GET_REQ = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&searchIn=title&from={FROM}&apiKey={news_api}"

price_params = {
    'function': "TIME_SERIES_DAILY_ADJUSTED",
    'symbol': STOCK,
    'apikey': news_api,

}

def change_percentage_calc(current, previous):
    try:
        diff = round(abs(current - previous) / previous, 5) * 100.0
        return diff
    except ZeroDivisionError:
        return 0


price_response = requests.get(STOCK_ENDPOINT, params=price_params)
price = price_response.json()['Time Series (Daily)']
price_list = [value for (key, value) in price.items()]
price_yesterday = float(price_list[0]['4. close'])
price_day_before_yesterday = float(price_list[1]['4. close'])
if price_yesterday > price_day_before_yesterday:
    symbol = "🔺"
else:
    symbol = "🔻"
price_change_percentage = change_percentage_calc(price_yesterday, price_day_before_yesterday)

response = requests.get(GET_REQ)
print(response.status_code)
print(price_change_percentage)
if price_change_percentage > 1:
    news = response.json()['articles'][:5]
    clean_news = [(item['title'], item['description']) for item in news]
    for item in clean_news:
        message = f'{STOCK}: {symbol} {round(price_change_percentage, 2)}%\nHeadline: {item[0]}\nBrief: {item[1]}\n'
        telegram_bot_send_text(message)
