import requests

bot_token = "****"
bot_chatID = "**"


def telegram_bot_send_text(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID \
                + '&parse_mode=Markdown&text=' + bot_message

    bot_response = requests.get(send_text)
    print(bot_response.status_code)
    return bot_response.json()
