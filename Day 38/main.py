import requests
from datetime import datetime

APP_ID= "f0dfd476"
API_KEY= "7a3c3e464740108aae7f395ccfad3214"

GENDER = "Male"
WEIGHT_KG = 74
HEIGHT_CM = 1.71
AGE = 23


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/46b335bbca1da283345b8cde03c89291/newWorkoutsProject/workouts"

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
result = response.json()['exercises']


today = datetime.now()


for exercise in result:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%x"),
            "time": today.strftime("%X"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(f"Response: {response.text}")





