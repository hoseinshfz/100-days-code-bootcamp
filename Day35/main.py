import requests
import os


def telegram_bot_messenger(bot_message):
    bot_token = os.environ.get("BOT_TOKEN")
    bot_chat_id = os.environ.get("BOT_CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id \
                + '&parse_mode=Markdown&text=' + bot_message

    bot_response = requests.get(send_text)
    return bot_response.json()


api_key = os.environ.get("API_KEY")
OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

params = {
    "lon": 0,
    "lat": 0,
    "appid": api_key,
}
MESSAGE = "It will rain, Take an Umbrella!"
response = requests.get(OWN_Endpoint, params=params)

weather_data = response.json()
weather_slice = weather_data['list'][:4]
will_rain = [True for forcast in weather_slice if int(forcast['weather'][0]['id']) < 700]

if len(will_rain) > 0:
    telegram_bot_messenger(MESSAGE)

