from app import db


class Truck(db.Model):
    __tablename__ = 'truck'
    license_plate = db.Column(db.String, primary_key=True)
    documents = db.relationship('Document', backref='truck', lazy=True)


class Driver(db.Model):
    __tablename__ = 'driver'
    id = db.Column(db.String, primary_key=True)
    phone = db.Column(db.String, nullable=False)
    document = db.relationship('Document', backref='driver', lazy=True)


class Trailer(db.Model):
    __tablename__ = 'trailer'
    license_plate = db.Column(db.String, primary_key=True)
    document = db.relationship('Document', backref='trailer', lazy=True)


class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)
    exp_date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    truck_id = db.Column(db.String, db.ForeignKey('truck.license_plate'), nullable=True)
    trailer_id = db.Column(db.String, db.ForeignKey('trailer.license_plate'), nullable=True)
    driver_id = db.Column(db.String, db.ForeignKey('driver.id'), nullable=True)
    notification = db.relationship('Notification', 
                                   primaryjoin="Document.id == Notification.id",
                                   backref="notification")


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, db.ForeignKey('document.id'), primary_key=True)  # add ForeignKey
    days_before = db.Column(db.Integer, nullable=False)


class AutoTrain(db.Model):
    __tablename__ = 'autotrain'
    truck_id = db.Column(db.String, db.ForeignKey('truck.license_plate'), primary_key=True)
    trailer_id = db.Column(db.String, db.ForeignKey('trailer.license_plate'), primary_key=True)
    driver_id = db.Column(db.String, db.ForeignKey('driver.id'), primary_key=True)
    # phone_id = db.Column(db.String, db.ForeignKey('driver.phone'), primary_key=True)
    truck = db.relationship('Truck', primaryjoin="AutoTrain.truck_id == Truck.license_plate",
                            backref='autotrain')
    trailer = db.relationship('Trailer', primaryjoin="AutoTrain.trailer_id == Trailer.license_plate",
                              backref='autotrain')
    driver = db.relationship('Driver', primaryjoin="AutoTrain.driver_id == Driver.id", backref='autotrain')
    # phone = db.relationship('Driver', primaryjoin="AutoTrain.phone_id == Driver.phone", backref='autotrain')

    # def __repr__(self):
    #     return '<{} {} {}>'.format(self.truck_id, self.trailer_id, self.driver_id)
