import os

import requests

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY")
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercise you did? ")

parameters = {
    "query" : exercise_text,
    "gender": os.environ.get("GENDER"),
    "weight": os.environ.get("WEIGHT"),
    "height": os.environ.get("HEIGHT"),
    "age": os.environ.get("AGE"),
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)