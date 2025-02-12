import requests  # Import the requests library for making HTTP requests
from datetime import datetime  # Import the datetime module for handling dates and times
import os  # Import os module to work with environment variables

# Retrieve environment variables for authentication and endpoint
APP_ID = os.environ.get('APP_ID')  # Nutritionix API Application ID
API_KEY = os.environ.get('API_KEY')  # Nutritionix API Application Key

SHEET_ENDPOINT = os.environ.get('SHEET_ENDPOINT')  # The endpoint for the Sheety API
SHEET_TOKEN = os.environ.get('SHEET_TOKEN')  # The Sheety API Bearer Token for authorization

# Personal information for making exercise queries
GENDER = "Male"  # Gender for exercise tracking
WEIGHT_KG = 74  # Weight in kilograms
HEIGHT_CM = 171  # Height in centimeters
AGE = 23  # Age of the user

# Nutritionix API endpoint for exercise tracking
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# Sheety API endpoint for logging workouts in Google Sheets
sheet_endpoint = f"https://api.sheety.co/46b335bbca1da283345b8cde03c89291/newWorkoutsProject/{SHEET_ENDPOINT}"

# Ask the user to input the exercises they've done
exercise_text = input("Tell me which exercises you did: ")

# Authorization header for Sheety API requests
sheet_header = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

# Headers for the Nutritionix API request
headers = {
    "x-app-id": APP_ID,  # Nutritionix Application ID
    "x-app-key": API_KEY,  # Nutritionix Application Key
}

# Parameters for the Nutritionix exercise query
parameters = {
    "query": exercise_text,  # The exercises provided by the user
    "gender": GENDER,  # Gender of the user
    "weight_kg": WEIGHT_KG,  # Weight of the user
    "height_cm": HEIGHT_CM,  # Height of the user
    "age": AGE  # Age of the user
}

# Make a POST request to the Nutritionix API to get exercise details
response = requests.post(exercise_endpoint, json=parameters, headers=headers)

# Raise an exception if the response status is not successful
response.raise_for_status()

# Parse the returned exercises from the Nutritionix response
result = response.json()['exercises']

# Get the current date and time for logging purposes
today = datetime.now()

# Iterate over the list of exercises returned by Nutritionix
for exercise in result:
    # Prepare the data to be sent to Sheety for logging the workout
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%x"),  # Format the date as MM/DD/YY
            "time": today.strftime("%X"),  # Format the time as HH:MM:SS
            "exercise": exercise['name'].title(),  # Capitalize the exercise name
            "duration": exercise["duration_min"],  # Duration of the exercise in minutes
            "calories": exercise['nf_calories']  # Calories burned during the exercise
        }
    }

    # Make a POST request to the Sheety API to log the exercise data in Google Sheets
    response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheet_header)

    # Print the response from the Sheety API (success or error message)
    print(f"Response: {response.text}")
