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
    
class Truck(db.Model):
    __tablename__ = 'truck'
    license_plate = db.Column(db.String, primary_key=True)
    documents = db.relationship('Document', backref='truck', lazy=True)
    
class Driver(db.Model):

class Trailer(db.Model):

    
class AutoTrain(db.Model):
    
    
