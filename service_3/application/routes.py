from application import app
from flask import request, Response
import random 

@app.route('/class', methods=["GET"])
def get_class():
    classes = ['Warrior', 'Wizard', 'Witch', 'Knight', 'Royal Knight', 'Warlock', 'Maid', 'Doctor']
    return Response(str(random.choice(classes)), mimetype='text/plain')