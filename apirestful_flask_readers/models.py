import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Readers(db.Model):
    __tablename__ = 'readers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
