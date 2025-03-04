# M7B Lecture Activities

def parse_student(string):
    dict = {}
    id = ''
    name = ''
    birthday = ''
    for char in string[0:8]:
        id += char
    dict['id'] = int(id)
    for char in string[8::]:
        if char == ' ':
            name += ' '
        if char.isalpha():
            name += char
    dict['name'] = name
    for char in string[8::]:
        if len(birthday) == 2:
            birthday += '/'
        if char.isdigit():
            birthday += char
    dict['birthday'] = birthday
    return dict

# print(parse_student('12345678Will Albright0116'))

def count_items(li):
    dict = {}
    for item in li:
        if item not in dict.keys():
            dict[item] = 0
        if item in dict.keys():
            dict[item] += 1
    print(dict)

# count_items([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3])

def list_fighters(battle_data):
    participants = set()
    for key in battle_data.keys():
        participants.add(key)
    for key in battle_data.values():
        for value in key.values():
            for item in value:
                participants.add(item)
    participants = list(participants)
    participants.sort()
    return participants

print(list_fighters({
    "Trisharp": {
        "loss": ["Togehug", "Psygoose"],
        "win": ["Pikaju", "Bulbizard"],
    },
    "Infernchimp": {
        "loss": ["Togehug", "Pikaju"],
        "win": ["Bulbizard", "Tehog"],
    },
    "Tehog": {
        "loss": ["Togehug", "Charasaur"],
        "win": ["Bulbizard", "Pikaju"]
    },
    "Psygoose": {
        "loss": ["Togehug", "Pikaju"],
        "win": ["Bulbizard", "Infernchimp"]
    },
}
))
