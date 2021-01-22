from application import app, db
from application.models import Characters
from flask import Flask, render_template, request
import requests

@app.route('/')
def index():
    char_response = requests.get("http://service2-backend:5000/name")
    item_response = requests.get("http://service2-backend:5000/item")
    class_response = requests.get("http://service3-backend:5000/class")

    stats_post = requests.post('http://service4-backend:5000/stats', json={"item_response":item_response.text, "class_response": class_response.text})
    
    character = Characters(name = char_response.text, item=item_response.text, class_type=class_response.text, bonus=stats_post.text)

    db.session.add(character)
    db.session.commit()
    descending_chars = Characters.query.order_by(Characters.id.desc()).limit(5)
    return render_template("index.html", cname=char_response.text, citem=item_response.text, classes=class_response.text, bonuses=stats_post.text, chars_list=descending_chars)