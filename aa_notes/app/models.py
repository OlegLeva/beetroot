from app import db


class Truck(db.Model):
    __tablename__ = 'truck'
    id = db.Column(db.Integer, primary_key=True) #db.ForeignKey('autotrain.id'),
    license_plate = db.Column(db.String, nullable=True)
    documents = db.relationship('Document',
                                primaryjoin="Truck.license_plate == Document.truck_id",
                                backref='truck', cascade="all, save-update, delete")


class Driver(db.Model):
    __tablename__ = 'driver'
    id = db.Column(db.Integer, primary_key=True)
    driver_name = db.Column(db.String, nullable=True)
    document = db.relationship('Document',
                               primaryjoin="Driver.driver_name == Document.driver_id",
                               backref='driver', cascade="all, save-update, delete")


class Trailer(db.Model):
    __tablename__ = 'trailer'
    id = db.Column(db.Integer, primary_key=True)
    license_plate1 = db.Column(db.String,  nullable=True)
    document = db.relationship('Document',
                               primaryjoin="Trailer.license_plate1 == Document.trailer_id",
                               backref='trailer', cascade="all, save-update, delete")


class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)
    exp_date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    truck_id = db.Column(db.String, db.ForeignKey('truck.license_plate'), nullable=True, )
    trailer_id = db.Column(db.String, db.ForeignKey('trailer.license_plate1'), nullable=True)
    driver_id = db.Column(db.String, db.ForeignKey('driver.driver_name'), nullable=True)

    notification = db.relationship('Notification',
                                   primaryjoin="Document.id == Notification.id", cascade="all, save-update, delete",
                                   backref="notification")


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, db.ForeignKey('document.id'), primary_key=True)
    days_before = db.Column(db.Integer, nullable=False)


class AutoTrain(db.Model):
    __tablename__ = 'autotrain'
    id = db.Column(db.Integer,  primary_key=True)
    truck_id = db.Column(db.String, db.ForeignKey('truck.license_plate'), unique=True)
    trailer_id = db.Column(db.String, db.ForeignKey('trailer.license_plate1'), unique=True)
    driver_id = db.Column(db.String, db.ForeignKey('driver.driver_name'), unique=True)
    phone_id = db.Column(db.String, nullable=False, unique=True)
    truck = db.relationship('Truck', primaryjoin="AutoTrain.truck_id == Truck.license_plate",
                            backref='autotrain', cascade="all, save-update, delete")
    trailer = db.relationship('Trailer', primaryjoin="AutoTrain.trailer_id == Trailer.license_plate1",
                              backref='autotrain', cascade="all, save-update, delete")
    driver = db.relationship('Driver', primaryjoin="AutoTrain.driver_id == Driver.driver_name",
                             backref='autotrain', cascade="all, save-update, delete")

    def __repr__(self):
        return '<{} {} {} {}>'.format(self.truck_id, self.trailer_id, self.driver_id, self.phone_id)
