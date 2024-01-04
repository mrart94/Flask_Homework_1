from flask import Flask
from flask import render_template

from functions import *

# Начало программы
app = Flask(__name__)


#Выводит мою карточку
@app.route("/mi")
def index():
    return render_template("index.html", title="Dmitry")


#Выводит всех кандидатов
@app.route("/")
def candidates():
    temp = load_candidates_from_json()
    return render_template("list.html", temp=temp)


#Выводит карточку кандидата по id
@app.route("/candidate/<int:x>")
def candidate(x):
    temp = get_candidate(x)
    return render_template("card.html", temp=temp)


#Выводит кандидатов с указанным именем
@app.route("/search/<candidate_name>")
def name_(candidate_name):
    temp = get_candidates_by_name(candidate_name)
    count = len(temp)
    return render_template("search.html", count=count, temp=temp)


#Выводит кандидатов с указанным скиллом
@app.route("/skill/<skill_name>")
def skill(skill_name):
    temp = get_candidates_by_skill(skill_name)
    count = len(temp)
    return render_template("skill.html", count=count, temp=temp, skill_name=skill_name)


app.run()
