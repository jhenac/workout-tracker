import requests
from datetime import datetime
import os

#____________GLOBAL VARIABLES____________#
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
GENDER = "female"
WEIGHT_KG = 45
HEIGHT_CM = 145
AGE = 33

#__________________________________________________________________________#
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
 "query": exercise_text,
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE,
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()
print(result)

#____________________________________________________________________________#
sheet_endpoint = "https://api.sheety.co/1160784756cc0aaed73ce9d38720fa6c/workoutTracking/workouts"

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

for exercise in result['exercises']:
    sheet_inputs = {
      "workout": {
        "date": today,
        "time": time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
      }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)

#________Basic Auhentication________________#

auth_response = requests.get(f'https://httpbin.org/basic-auth/{APP_ID}/{API_KEY}', auth=(APP_ID, API_KEY))
print(auth_response.status_code)

