import os
import sqlalchemy
from flask_migrate import Migrate 
from models import db, Item
from flask import Flask, jsonify, request
from sqlalchemy import desc 
  
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/change_this_name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def list():
    items = Item.query.all()
    response = []
    for i in items:
        response.append("%s" % i)
    
    return jsonify(response)
    
@app.route('/add', methods=['POST'])
def add():
    info = request.get_json() or {}
    item = Item(text=info["elephant"])
    db.session.add(item)
    db.session.commit()
    return jsonify({"response":"ok"})
    
@app.route('/lifo-pop', methods = ['GET'])
def pop ():
    last = Item.query.order_by(desc(Item.created_on)).first()
    if last is not None:
        db.session.delete(last)
        db.session.commit()
    return jsonify({"deleted": "%s" % last})
    
@app.route('/fifo-pop', methods = ['GET'])
def po (): 
    first = Item.query.first()
    if first is not None:
        db.session.delete(first)
        db.session.commit()
    return jsonify(({"deleted": "%s" % first}))
    
@app.route('/fifo-pop', methods=['GET'])
def destroy():
    first = Item.query.first()
    if first is not None:
        db.session.delete(first)
        db.session.commit()
    return jsonify({"deleted":"%s"%first})
    
    

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
=======
import os 
from flask import Flask, jsonify, request

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'My First Back-End Proj.'

@app.route('/people')
def hello():
    people = [
    {
    "title":"most influential personalities behind coding with their date of birth",
    },
    {
    "name": "Ada Lovelace", 
    "dob": "December 10, 1815, London, United Kingdom"
    },
    {
    "name": "Margaret Hamilton", 
    "dob": "December 9, 1902, Cleveland, Ohio"
    },
    {
    "name": "Grace Hopper", 
    "dob": " December 9, 1906, NY, NY"
    },
    {
    "name": "Joan Clarke", 
    "dob": " June 24, 1917, West Norwood, London, England"
    },
    {
    "name": "Edith Clarke", 
    "dob": " February 10, 1883, West Norwood, Ellicott City, Maryland"
    },
    ]
    return jsonify (people)
    
@app.route('/places')
def bye(): 
    places = [
        {
        "title":"top rated restaurants in miami (above 4.4 stars)",
        },
        {
        "name": "The Wharf",
        "rating": 4.4
        },
        {
        "name": "Il Gabbiano",
        "rating": 4.5
        },
        {
        "name": "Milanezza - Key Biscayne",
        "rating": 4.5
        },
        {
        "name": "Alter",
        "rating": 4.4
        },
        {
        "name": "Santorini by Georgios",
        "rating": 4.7
        },
        ]
    return jsonify (places)
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
>>>>>>> origin/master

