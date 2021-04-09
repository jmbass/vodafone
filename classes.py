class Geo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    lat = db.Column('lat', db.Float)
    lng = db.Column('lng', db.Float)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
        nullable=False)
    def __init__(self):
        self.lat = 0
        self.lng = 0

class Address(db.Model):
    _id  = db.Column("id", db.Integer, primary_key=True)
    city = db.Column("city", db.String(10))
    street = db.Column("street", db.String(10))
    suite = db.Column("suite", db.String(10))
    zipcode = db.Column("zipcode", db.String(10))
    geo = db.relationship('Geo', uselist=False, backref='address', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    def __init__(self):
        self.city = ''
        self.street = ''
        self.suite = ''
        self.zipcode = ''
        

class Company(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    bs = db.Column("bs", db.String(100))
    catchPhrase = db.Column("catch_phrase", db.String(100))
    name = db.Column("name", db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    def __init__(self):
        self.bs = ''
        self.catchPhrase = ''
        self.name = ''

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(10))
    website = db.Column("website", db.String(10))
    phone = db.Column("phone", db.String(10))
    email = db.Column("email", db.String(10))
    username =  db.Column("username", db.String(10))
    address = db.relationship('Address', uselist=False, backref='user', lazy=True)
    company = db.relationship("Company", uselist=False, backref='user', lazy=True)

    def __init__(self, id, name, website, phone, email, username, address, company):
        self._id = id
        self.name = name
        self.website = website
        self.phone = phone
        self.email = email
        self.username = username
        self.address = address
        self.company = company