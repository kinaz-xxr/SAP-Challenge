from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BayTable1(db.Model):
    __tablename__ = 'BayTable1'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable2(db.Model):
    __tablename__ = 'BayTable2'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable3(db.Model):
    __tablename__ = 'BayTable3'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable4(db.Model):
    __tablename__ = 'BayTable4'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable5(db.Model):
    __tablename__ = 'BayTable5'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable6(db.Model):
    __tablename__ = 'BayTable6'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable7(db.Model):
    __tablename__ = 'BayTable7'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable8(db.Model):
    __tablename__ = 'BayTable8'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable9(db.Model):
    __tablename__ = 'BayTable9'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BayTable10(db.Model):
    __tablename__ = 'BayTable10'
    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class RevenueLossTable(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.String(40))
    revenue = db.Column(db.Integer)
    loss = db.Column(db.Integer)
    compact_loss = db.Column(db.Integer)
    medium_loss = db.Column(db.Integer)
    fullsize_loss = db.Column(db.Integer)
    class1_loss = db.Column(db.Integer)
    class2_loss = db.Column(db.Integer)
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}