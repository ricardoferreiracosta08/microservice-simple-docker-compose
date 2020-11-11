import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
