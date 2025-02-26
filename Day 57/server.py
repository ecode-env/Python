from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(1,9)
    return render_template(template_name_or_list="index.html",num=random_number,  CURRENT_YEAR=current_year )


@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(url=f"https://api.genderize.io/?name={name}").json()['gender']
    age = requests.get(url=f"https://api.agify.io?name={name}").json()["age"]
    return render_template(template_name_or_list="guess.html",
                           name=name,
                           age=age,
                           gender=gender
                           )

if __name__ == "__main__":
    app.run(debug=True)