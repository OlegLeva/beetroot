from app import db
from datetime import date


from app.models import Driver, Document, Trailer, Truck, Notification


truck1 = Truck(license_plate="BI4078CE"),
truck2 = Truck(license_plate="BI8576EI"),
truck3 = Truck(license_plate="BI7185AO")
trucks = [truck1, truck2, truck3]
for t in trucks:
    db.session.add(t)
db.session.commit()


trailer1 = Trailer(license_plate="BI2324XK"),
trailer2 = Trailer(license_plate="BI3844XM"),
trailer3 = Trailer(license_plate="BI4663XK")
trailers = [truck1, truck2, truck3]
for t in trailers:
    db.session.add(t)
db.session.commit()


driver1 = Driver(phone="+380980353438", name="Терещенко Дмитрий")
driver2 = Driver(phone="+380679265219", name="Возный Андрей")
driver3 = Driver(phone="+380974537879", name="Возный Виталий")
drivers = [driver1, driver2, driver3]
for d in drivers:
    db.session.add(d)
db.session.commit()


documemt1 = Document(name="protocol", exp_date=date(2020,10,20), truck_id=truck1.license_plate)
documemt2 = Document(name="protocol", exp_date=date(2020,10,20), truck_id=truck2.license_plate)
documemt3 = Document(name="protocol", exp_date=date(2020,10,20), truck_id=truck3.license_plate)
documemts = [documemt1, documemt2, documemt3]
for d in documemts:
    db.session.add(d)
db.session.commit()


notification1 = Notification(days_before=30, id=documemt1.id)
notification2 = Notification(days_before=30, id=documemt2.id)
notification3 = Notification(days_before=30, id=documemt3.id)
notifications = [notification1, notification2, notification3]
for d in notifications:
    db.session.add(d)
db.session.commit()

