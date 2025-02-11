import requests


APP_ID= "f0dfd476"
API_KEY= "c2572e9c344bfc7ae49c72a948eb5190"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/823f6199e759c8f1e33ee34d5cc0c4ed/workoutTracking/workouts"


header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise = {
    "query": "Ran 2 miles and walked for 3km."
}

sheet_inputs = {
    "workout": {
        "date": "11/01/2025",
        "time": "10:23",
        "exercise": "walk",
        "duration": 22,
        "calories": 130
    }
}



response =  requests.post(sheet_endpoint, json=sheet_inputs)
response.raise_for_status()
print(response.json())

#response = requests.post(url=nutritionix_endpoint, json=exercise, headers=header)

#print(response.json())