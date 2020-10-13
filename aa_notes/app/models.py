from app import db


class Truck(db.Model):
    __tablename__ = 'truck'
    license_plate = db.Column(db.String, primary_key=True)
    documents = db.relationship('Document',
                                primaryjoin="Truck.license_plate == Document.truck_id", cascade="all,delete",
                                backref='truck', passive_deletes=True)


class Driver(db.Model):
    __tablename__ = 'driver'
    id = db.Column(db.String, primary_key=True)
    document = db.relationship('Document',
                               primaryjoin="Driver.id == Document.driver_id", cascade="all,delete",
                               backref='driver', passive_deletes=True)


class Trailer(db.Model):
    __tablename__ = 'trailer'
    license_plate1 = db.Column(db.String, primary_key=True)
    document = db.relationship('Document',
                               primaryjoin="Trailer.license_plate1 == Document.trailer_id", cascade="all,delete",
                               backref='trailer', passive_deletes=True)


class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)
    exp_date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    truck_id = db.Column(db.String, db.ForeignKey('truck.license_plate'), nullable=True)
    trailer_id = db.Column(db.String, db.ForeignKey('trailer.license_plate1'), nullable=True)
    driver_id = db.Column(db.String, db.ForeignKey('driver.id'), nullable=True)

    notification = db.relationship('Notification',
                                   primaryjoin="Document.id == Notification.id", cascade="all,delete",
                                   backref="notification")


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, db.ForeignKey('document.id'), primary_key=True)  # add ForeignKey
    days_before = db.Column(db.Integer, nullable=False)


class AutoTrain(db.Model):
    __tablename__ = 'autotrain'
    id = db.Column(db.Integer, primary_key=True)
    truck_id = db.Column(db.String, db.ForeignKey('truck.license_plate'))
    trailer_id = db.Column(db.String, db.ForeignKey('trailer.license_plate1'))
    driver_id = db.Column(db.String, db.ForeignKey('driver.id'))
    phone_id = db.Column(db.String, nullable=False)
    truck = db.relationship('Truck', primaryjoin="AutoTrain.truck_id == Truck.license_plate", cascade="all,delete",
                            backref='autotrain')
    trailer = db.relationship('Trailer', primaryjoin="AutoTrain.trailer_id == Trailer.license_plate1", cascade="all,delete",
                              backref='autotrain')
    driver = db.relationship('Driver', primaryjoin="AutoTrain.driver_id == Driver.id", cascade="all,delete",
                             backref='autotrain')

    def __repr__(self):
        return '<{} {} {} {}>'.format(self.truck_id, self.trailer_id, self.driver_id, self.phone_id)
