from application import app
from flask import request, Response
import random 

@app.route('/name', methods=["GET"])
def get_name():
    gender = ["Male", "Female", "Game Character"]
    male_names = ["Frederik", "Rodriguez", "Miguel", "Dave", "Harry", "Roberto"]
    female_names = ["Linda", "Elena", "Rosa", "Vy", "Lola", "Adrianne"]
    game_character_names = ["Ezio", "Master Chief", "Trevor", "Ratchet", "Captiain Price", "Goku"]
    random_gender = str(random.choice(gender))
    if random_gender == 'Male':
        chosen_name = str(random.choice(male_names))
    elif random_gender == 'Female':
        chosen_name = str(random.choice(female_names))
    else:
        chosen_name = str(random.choice(game_character_names))
    return Response(chosen_name, mimetype='text/plain')

@app.route('/item', methods=["GET"])
def get_item():
    bonus_item = ['Sword', 'Axe', 'Bow', 'Sponge', 'Mirror', 'Wand', 'PokeBall']
    return Response(str(random.choice(bonus_item)), mimetype='text/plain') 