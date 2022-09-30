from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(0, 99)
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_response_data = gender_response.json()
    guessed_gender = gender_response_data["gender"]

    # Short version of above
    guessed_age = requests.get(f"https://api.agify.io?name={name}").json()["age"]


    return render_template("guess.html", name=name, gender=guessed_gender, age=guessed_age)


if __name__ == "__main__":
    app.run(debug=True)