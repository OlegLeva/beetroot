from a_notes.app.routes import db


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, primary_key=True)
    days_before = db.Column(db.Integer, nullable=False)
    document = db.relationship("Document", uselist=False, backref="notification")


class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)
    exp_date = db.Column(db.Datetime, nullable=False)
    name = db.Column(db.String, nullable=False)
    notification = db.relationship('Notification', backref='document', lazy=True)


class Truck(db.Model):
    __tablename__ = 'truck'
    license_plate = db.Column(db.String, primary_key=True)
    document = db.relationship('Document', backref='truck', lazy=True)


class Driver(db.Model):
    __tablename__ = 'driver'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String, nullable=False)
    document = db.relationship('Document', backref='driver', lazy=True)


class Trailer(db.Model):
    __tablename__ = 'trailer'
    licence_plate = db.Column(db.String, primary_key=True)
    document = db.relationship('Document', backref='trailer', lazy=True)


class AutoTrain(db.Model):
    __tablename__ = 'autotrain'
    truck_id = db.Column(db.String, primary_key=True)
    trailer_id = db.Column(db.String, primary_key=True)
    driver_id = db.Column(db.Integer, primary_key=True)
    truck = db.relationship('Truck', uselist=False, back_populates='autotrain')
    trailer = db.relationship('Trailer', uselist=False, back_populates='autotrain')
    driver = db.relationship('Driver', uselist=False, back_populates='autotrain')
