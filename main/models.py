from main import db
from flask_sqlalchemy import SQLAlchemy

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    want = db.Column(db.Text)

    def __repr__(self):
        return "Entry id={} name={!r} want={!r}>".format(self.id, self.name, self.want)

def init():
    db.create_all()