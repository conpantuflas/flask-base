from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return "<user %r>" % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
        }    