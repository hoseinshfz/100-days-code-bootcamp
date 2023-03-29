import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
USERNAME = os.environ["USER_NAME"]
PASSWORD = os.environ["PASSWORD"]

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
    "x-remote-user-id" : "0",
}
user_input = input("what did you do?\n")

param = {
 "query": user_input,
 "gender": "male",
 "weight_kg": 62.0,
 "height_cm": 172.0,
 "age": 31
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, headers=headers, json=param)
workouts = response.json()
print(workouts)

sheety_url = "https://api.sheety.co/033ec52ddde7e5375fa02d98d2dbee4d/myWorkoutsUdemy/workouts"
# response = requests.get(url=sheety_url)
# print(response.json())

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in workouts["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_url, json=sheet_inputs,
                                    auth=(USERNAME, PASSWORD))
    print(sheety_response.text)

