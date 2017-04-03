from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120), index = True, unique = True)
    location = db.Column(db.String(120), index = True, unique = False, default = "Russia")
    profession = db.Column(db.String(200), index = True, unique = False)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
'''link 1-many, where many=Posts one=author. 'dynamic' is special and useful if you have many items.
Instead of loading the items SQLAlchemy will return another query object which you can further refine before loading
the items. This is usually what you want if you expect more than a handful of items for this relationship. '''

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    body = db.Column(db.String(140))
    tag = db.Column(db.String(64), default = "IT")
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

