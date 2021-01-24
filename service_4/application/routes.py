from application import app
from flask import request, Response
import random

@app.route('/stats', methods=["GET", "POST"])
def get_bonus():
    collection = request.get_json()
    #'bonus' Section
    item_bonus = {'Wand':'+120 Magic', 'Sword':'+120 Attack', 'Axe':'+120 Woodcutting', 'Bow':'+120 Range', 'Sponge':'+120 Cleanliness', 'Mirror':'Reflective Armour','PokeBall':'Power to capture anything', 'Assassins Blade':'+100 Stealth', 'AK47':'+500 Range', 'Super Saiyan Powers':'Unbeatable'}
    type_bonus = {'Warrior':'+100 Attack', 'Wizard':'+100 Magic', 'Witch':'+100 Alchemy', 'Knight':'+150 Attack', 'Royal Knight':'+250 Attack', 'Warlock':'+300 Magic', 'Maid':'+100 Cleaning', 'Doctor':'+150 Healing', 'Pokemon Master':'+ Pokedex', 'Soldier':'+1000 Mental Strength', 'Saiyan':'Zenkai Boost'}
    
    new_item = collection["item_response"]
    new_type = collection["class_response"]
    chosen_item = item_bonus[new_item]
    chosen_type = type_bonus[new_type]

    extra_bonus = ''
    # Item Bonus for Each Class
    wand_bonus = {'Warrior':'+5 Magic', 'Wizard':'+200 Magic', 'Witch':'+150 Magic', 'Knight':'+1 Magic', 'Royal Knight':'-30 Magic', 'Warlock':'+200 Magic', 'Maid':'+30 Magic', 'Doctor':'+30 Magic'}
    sword_bonus = {'Warrior':'+100 Attack', 'Wizard':'+5 Attack', 'Witch':'+5 Attack', 'Knight':'+150 Attack', 'Royal Knight':'+200 Attack', 'Warlock':'+10 Attack', 'Maid':'+80 Attack', 'Doctor':'+30 Attack'}
    axe_bonus = {'Warrior':'+40 Attack', 'Wizard':'+10 Attack', 'Witch':'+10 Attack', 'Knight':'+50 Attack', 'Royal Knight':'+60 Attack', 'Warlock':'+10 Magic', 'Maid':'+100 Attack', 'Doctor':'+30 Attack'}
    bow_bonus = {'Warrior':'+30 Ranged', 'Wizard':'+10 Ranged', 'Witch':'+10 Ranged', 'Knight':'+50 Ranged', 'Royal Knight':'+60 Ranged', 'Warlock':'+10 Ranged', 'Maid':'+100 Ranged', 'Doctor':'+30 Ranged'}
    sponge_bonus = {'Warrior':'Shiny Armour', 'Wizard':'Shiny Wizard Hat', 'Witch':'Shiny Cauldron', 'Knight':'Shiny Armour', 'Royal Knight':'Extremely Shiny Armour', 'Warlock':'Cleaning Spell', 'Maid':'Invincibility', 'Doctor':'Disinfectant'}
    pokeball_bonus = {'Warrior':'Catch a Pokemon', 'Wizard':'Catch a Pokemon', 'Witch':'Catch a Pokemon', 'Knight':'Catch a Pokemon', 'Royal Knight':'Catch a Pokemon', 'Warlock':'Catch a Pokemon', 'Maid':'Catch a Pokemon', 'Doctor':'Catch a Pokemon', 'Pokemon Master':'The Greatest there ever was', 'Soldier':'Contains a Purrloin', 'Saiyan': 'Contains a Beerus'}

    if new_item == 'Wand':
        extra_bonus = wand_bonus[new_type]
    elif new_item == 'Axe':
        extra_bonus = axe_bonus[new_type]
    elif new_item == 'Sword':
        extra_bonus = sword_bonus[new_type]
    elif new_item == 'Bow':
        extra_bonus = bow_bonus[new_type]
    elif new_item == 'Sponge':
        extra_bonus = sponge_bonus[new_type]
    elif new_item == 'PokeBall':
        extra_bonus = pokeball_bonus[new_type]
    else:
        extra_bonus = 'No Extra Bonuses'
    
    final_bonus = chosen_type + ', ' + chosen_item + ', ' + extra_bonus
    
    return Response(final_bonus, mimetype='text/plain')
