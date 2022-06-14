import os #os es un objeto de python
from flask import Flask, jsonify, request #clase de flask, app es una instacia con propiedades de flask, una instancia es un objeto de su clase
from models import db, User
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

BASEDIR = os.path.abspath(os.path.dirname(__file__)) #directorio base
app = Flask(__name__)

#configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASEDIR, "test.db")
app.config["DEBUG"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) #creamos una conexion con la bese de datos
CORS(app) #no tener errores en el cors
Migrate(app, db) #migrate crea la base de datos

@app.route("/user", methods=["POST"])
def user():
    user = User()
    user.email = request.json.get("email")
    user.password = request.json.get("password")

    db.session.add(user) #guarda la instancia de la clase como insercion
    db.session.commit()  

    return jsonify(user.serialize()), 200

@app.route("/users", methods=["GET"])   
def users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users)) 
    return jsonify(users)

@app.route("/user/<int:id>", methods=["PUT","DELETE"])    
def update_user(id):
    if request.method == "PUT":
        user = User.query.get(id)
        print(user.password, "vieja")
        user.password = request.json.get("password")
        print(user.password, "nueva")

        db.session.commit()

        return jsonify(user.serialize())
    else: user = User.query.get(id) 
    db.session.delete(user) 
    db.session.commit() 
    return jsonify({ "éxito": True }), 202


if __name__ == "__main__":
    app.run(host="localhost", port="5000")



