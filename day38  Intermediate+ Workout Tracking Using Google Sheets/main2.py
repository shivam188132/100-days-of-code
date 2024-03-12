import os
os.environ["APP_ID"] = "xxxxxxx"
os.environ["API_KEY"] = "xxxxxxxxxxxxxxxxxxxx"
os.environ["User"] = "xxxxxxxxxxxxxxx"
os.environ["Password"] = "xxxxxxxxxxxxxxxxxxxx"
os.environ["sheet_endpoint"] = "xxxxxxxxxxxxxxxxx"

import os
from datetime import datetime

import requests

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 182
AGE = 21

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
User = os.environ["USERNAME"]
Password = os.environ["PASSWORD"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=sheet_endpoint,
        json=sheet_inputs,
        auth=(User, Password)
    )

    print(f"Sheety Response: \n {sheet_response.text}")
