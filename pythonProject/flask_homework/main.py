from flask import Flask
import json


# Загружает данные из файла candidates.json:
def load_candidates():
    with open("candidates.json", encoding='utf-8') as f:
        json_to_dict = json.load(f)
    return json_to_dict

#Не пойму зачем она нужна?
def get_all():
    print(load_candidates())


#Получает кандидата в виде словаря
def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate


#Получает список кандидатов в виде списка, где каждый кандидат словарь, по названию скилла
def get_by_skill(skill_name):
    candidates_list_by_skill = []
    temp = load_candidates()
    for human in temp:
        if skill_name in (human['skills']).lower():
            candidates_list_by_skill.append(human)
    return candidates_list_by_skill


#Начало программы
app = Flask(__name__)


@app.route("/")
def list_human():
    str_load_candidates = []
    for candidate in load_candidates():
        str_load_candidates.append(f'<pre>Имя кандидата - {candidate['name']}<br>Позиция кандидата {candidate['position']}<br>Навыки через заяпятую {candidate['skills']}</pre>')
    return f'<html>{''.join(str_load_candidates)}</html>'


@app.route("/candidates/<int:x>")
def candida(x):
    temp = get_by_pk(x)
    return f'<html><img src="({temp['picture']})"><pre>Имя кандидата - {temp['name']}<br>Позиция кандидата {temp['position']}<br>Навыки через заяпятую {temp['skills']}</pre></html>'


@app.route("/skills/<x>")
def skills(x):
    temp = get_by_skill(x)
    to_return = []
    for candidate in temp:
        to_return.append((f'<pre>Имя кандидата - {candidate['name']}<br>Позиция кандидата {candidate['position']}<br>Навыки через заяпятую {candidate['skills']}</pre>'))
    return f'<html>{''.join(to_return)}</html>'
#
app.run()
