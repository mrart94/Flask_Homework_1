from flask import Flask
import json


# ЗАгружает данные из файла candidates.json:
def load_candidates():
    with open("candidates.json") as f:
        temp = json.load(f)
    return temp


print(load_candidates())


def get_all():
    print(load_candidates())


def get_by_pk(pk):
    for human in load_candidates():
        if human['pk'] == pk:
            return human


def get_by_skill(skill_name):
    human_list = []
    temp = load_candidates()
    for human in temp:
        if skill_name in (human['skills']).lower():
            human_list.append(human)
    return human_list


print(get_by_skill('python'))

app = Flask(__name__)


@app.route("/")
def list_human():
    for human in load_candidates():
        string_ = []
        string_.append("Имя кандидата -" + human['name'] + "\n" + "Позиция кандидата" + human[
            'position'] + "\n" + "Навыки через заяпятую" + human['skills'])
    return string_


@app.route("/candidates/<int:x>")
def candida(x):
    temp = get_by_pk(x)
    return f'<img src="{temp['picture']}">'


@app.route("/skills/<int:x>")
def skills(x):
    temp = get_by_skill(x)
    for i in temp:
        pass


app.run()
