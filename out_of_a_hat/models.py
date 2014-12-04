from out_of_a_hat import db
import uuid
import random

class Hat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    uuid = db.Column(db.String(32))
    items = db.relationship('Item', backref='hat', lazy='dynamic')

    def __init__(self, name):
        self.name = name
        self.uuid = uuid.uuid4().hex
    
    def __repr__(self):
        return '<Hat: {}>'.format(self.name)

    def get_random_item(self):
        if self.items.count() == 0:
            return None
        return random.choice(self.items.all())

    @staticmethod
    def get_by_uuid(uuid):
        return Hat.query.filter_by(uuid=uuid).first()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    hat_id = db.Column(db.Integer, db.ForeignKey('hat.id'))

    def __init__(self, name, hat):
        self.name = name
        self.hat = hat

    def __repr__(self):
        return '<Item: {}>'.format(self.name)
