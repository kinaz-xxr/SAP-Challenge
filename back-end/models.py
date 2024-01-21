from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BayTable1(db.Model):
    __tablename__ = 'BayTable1'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable2(db.Model):
    __tablename__ = 'BayTable2'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable3(db.Model):
    __tablename__ = 'BayTable3'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable4(db.Model):
    __tablename__ = 'BayTable4'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable5(db.Model):
    __tablename__ = 'BayTable5'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable6(db.Model):
    __tablename__ = 'BayTable6'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable7(db.Model):
    __tablename__ = 'BayTable7'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable8(db.Model):
    __tablename__ = 'BayTable8'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable9(db.Model):
    __tablename__ = 'BayTable9'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class BayTable10(db.Model):
    __tablename__ = 'BayTable10'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

class RevenueLossTable(db.Model):
    date = db.Column(db.String(40), primary_key=True)
    revenue = db.Column(db.Integer)
    loss = db.Column(db.Integer)