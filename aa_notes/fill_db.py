from app import db

# Todo: Создать базу данных один раз, вытащить базу данныз и отобразить на лицевой странице

from app.models import Driver, Document, Trailer, Truck, Notification

truck = [
    Truck(license_plate="BI4078CE"),
    Truck(license_plate="BI8576EI"),
    Truck(license_plate="BI7185AO")
]
for p in truck:
    db.session.add(p)
db.session.commit()

trailers = [
    Trailer(license_plate="BI2324XK"),
    Trailer(license_plate="BI3844XM"),
    Trailer(license_plate="BI4663XK")
]
for t in trailers:
    db.session.add(t)
db.session.commit()

drivers = [
    Driver(phone="+380980353438", name="Терещенко Дмитрий"),
    Driver(phone="+380679265219", name="Возный Андрей"),
    Driver(phone="+380974537879", name="Возный Виталий")
]
for d in drivers:
    db.session.add(d)
db.session.commit()

documemts = [
    Document(name="protokol", exp_date="25.12.2020"),
    Document(name="protokol", exp_date="15.12.2020"),
    Document(phone="protocol", exp_date="05.11.2020")
]
for d in documemts:
    db.session.add(d)
db.session.commit()

notifications = [
    Notification(days_before=30),
    Notification(days_before=30),
    Notification(days_before=30)
]
for d in documemts:
    db.session.add(d)
db.session.commit()

