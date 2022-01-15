import os
from datetime import datetime

import requests

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY")
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/a99841fe556d00090b02e62e647eca8c/workoutSheet/workouts"
exercise_text = input("Tell me which exercise you did? ")

parameters = {
    "query" : exercise_text,
    "gender": os.environ.get("GENDER"),
    "weight_kg": os.environ.get("WEIGHT"),
    "height_cm": os.environ.get("HEIGHT"),
    "age": os.environ.get("AGE"),
}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

#   ====================== Start of Sheet API Mechanism =================================

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

basic_headers = {
    "Authorization": os.environ.get("BASIC_AUTH")
}

bearer_headers = {
    "Authorization": os.environ.get("BEARER_AUTH")
}
for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # No Authentication
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)


    #   Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=basic_headers
    )
    print(sheet_response.text)


    # Bearer Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(sheet_response.text)


