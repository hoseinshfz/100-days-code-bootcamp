import pandas
import random
import datetime
import smtplib

letters_file_start_path = "letter_templates\letter_"
letters_file_end_path = ".txt"
birthday_file_name = "birthdays.csv"
other_email = "hosein.shfz+100dayscodetest@gmail.com"
sample_letters = []


def send_email(other_email, title, text):
    """sends email from the my_email"""
    my_email = "****@gmail.com"
    password = "XXXX"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs=other_email,
            msg=f"Subject:{title}\n\n{text}")
        print("message send successfully!")


def read_email_samples():
    for i in range(1, 4):
        with open(f'{letters_file_start_path}{i}{letters_file_end_path}') as file:
            letter = file.read()
            sample_letters.append(letter)


read_email_samples()
birthday_data = pandas.read_csv(birthday_file_name)

now = datetime.datetime.now().date()

BD_list = {row['name']: [row.email, datetime.datetime(year=row.year, month=row.month, day=row.day)]
           for (index, row) in birthday_data.iterrows()}

todays_BD_list = [item for item in BD_list.items()
                  if item[1][1].month == now.month and item[1][1].day == now.day]

letter = str(random.choice(sample_letters))

for person in todays_BD_list:
    new_letter = letter.replace("[NAME]", str(person[0]))
    new_letter = new_letter.replace("Angela", "Hans")
    send_email(person[1][0], "Happy Birthday!", new_letter)


