from application import app
from flask import request, Response
import random 

@app.route('/name', methods=["GET"])
def get_name():
    gender = ["Male", "Female"]
    male_names = ["Frederik", "Rodriguez", "Miguel", "Dave", "Harry", "Roberto"]
    female_names = ["Linda", "Elena", "Rosa", "Vy", "Lola", "Adrianne"]
    random_gender = str(random.choice(gender))
    if random_gender == 'Male':
        chosen_name = str(random.choice(male_names))
    else:
        chosen_name = str(random.choice(female_names))
    return Response(chosen_name, mimetype='text/plain')

@app.route('/item', methods=["GET"])
def get_item():
    bonus_item = ['Sword', 'Axe', 'Bow', 'Sponge', 'Mirror', 'Wand']
    return Response(str(random.choice(bonus_item)), mimetype='text/plain') 