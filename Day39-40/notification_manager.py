import requests
import smtplib

bot_token = "****"
bot_chatID = "****"
password = "****"
my_email = "****@gmail.com"


class NotificationManager:
    """send notifications via Telegram Bot or Email"""

    def telegram_bot_send_text(self, bot_message):
        """sends a message at Telegram"""
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID \
                    + '&parse_mode=Markdown&text=' + bot_message

        bot_response = requests.get(send_text)
        print(bot_response.status_code)
        return bot_response.json()

    def send_email(self, email, message_list):
        """sends email from the my_email"""
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            title = "New Low Price Flight!"
            msg = f"Subject:{title}\n\n"
            for message in message_list:
                msg += f"{message}\n\n\n"
            msg = msg.encode('utf-8')
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, to_addrs=email,
                msg=msg)
            print("message send successfully!")
