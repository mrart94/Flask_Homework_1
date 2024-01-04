import json


def load_candidates_from_json(): #возвращает список всех кандидатов
    with open("candidates.json", encoding='utf-8') as f:
        candidates_dict = json.load(f)
        return candidates_dict
print(load_candidates_from_json())


def get_candidate(candidate_id): #возвращает одного кандидата по его id
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate
print(get_candidate(1))


def get_candidates_by_name(candidate_name): #возвращает кандидатов по имени
    candidates_by_name = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            candidates_by_name.append(candidate)
    return candidates_by_name
print(get_candidates_by_name('Adela Hendricks'))

def get_candidates_by_skill(skill_name): #возвращает кандидатов по навыку
    candidates_by_skill = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower():
            candidates_by_skill.append(candidate)
    return candidates_by_skill
print(get_candidates_by_skill('python'))