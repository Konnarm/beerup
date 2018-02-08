from app import db

interests = db.Table('interests',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interest.id'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    interests = db.relationship(
        'Interest', secondary=interests, lazy='subquery',
        backref=db.backref('users', lazy=True)
    )

    def __repr__(self):
        return '<id {}, name {}>'.format(self.id, self.name)


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<id {}, name {}>'.format(self.id, self.name)
