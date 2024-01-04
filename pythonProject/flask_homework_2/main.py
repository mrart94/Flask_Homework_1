from flask import Flask
from flask import render_template

from functions import get_candidate, load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill

# Начало программы
app = Flask(__name__)

#Работает
@app.route("/index.html")
def index():
    return render_template("index.html", title="Dmitry")

#Работает
@app.route("/")
def candidates():
    temp = load_candidates_from_json()

    return render_template("list.html", temp=temp)

#Не работает фото
@app.route("/candidate/<int:x>")
def candidate(x):
    temp = get_candidate(x)
    return render_template("card.html", name=temp['name'], position=temp['position'], picture=temp['picture'],
                           skills=temp['skills'])

#Работает
@app.route("/search/<candidate_name>")
def name_(candidate_name):
    temp = get_candidates_by_name(candidate_name)
    count = len(temp)
    return render_template("search.html", count=count, temp=temp)


@app.route("/skill/<skill_name>")
def skill(skill_name):
    temp = get_candidates_by_skill(skill_name)
    count = len(temp)
    return render_template("skill.html", count=count, temp=temp, skill_name=skill_name)


app.run()
