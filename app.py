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