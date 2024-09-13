from . import db

class User(db.Model):
    id       = db.Column(db.Integer,     primary_key = True)
    username = db.Column(db.String(50),  unique = True, nullable = False)
    email    = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    role     = db.Column(db.String(20),  nullable = False)

    def __repr__(self):
        return f"<User {self.username}>"

class House(db.Model):
    id       = db.Column(db.Integer,     primary_key = True)
    address  = db.Column(db.String(150), nullable = False)
    owner_id = db.Column(db.Integer,     db.ForeignKey('user.id'))

class Payment(db.Model):
    id       = db.Column(db.Integer,    primary_key = True)
    amount   = db.Column(db.Float,      nullable = False)
    type     = db.Column(db.String(20), nullable = False)  # 'mensual', 'anual', 'extraordinario'
    status   = db.Column(db.String(20), nullable = False)  # 'pendiente', 'aprovado', 'rechazado'
    house_id = db.Column(db.Integer,    db.ForeignKey('house.id'))

class Visit(db.Model):
    id           = db.Column(db.Integer,     primary_key=True)
    visitor_name = db.Column(db.String(100), nullable=False)
    qr_code      = db.Column(db.String(100))
    approved     = db.Column(db.Boolean,     default=False)
    neighbor_id  = db.Column(db.Integer,     db.ForeignKey('user.id'))
    security_id  = db.Column(db.Integer,     db.ForeignKey('user.id'))
