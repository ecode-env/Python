from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_year = year = datetime.now().year
    random_number = random.randint(1,9)
    return render_template(template_name_or_list="index.html",num=random_number,  CURRENT_YEAR=current_year )


@app.route('/guess/<name>')
def guess(name):

    return render_template(template_name_or_list="index.html")


if __name__ == "__main__":
    app.run(debug=True)