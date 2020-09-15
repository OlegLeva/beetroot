from app import db

# Todo: Создать базу данных один раз, вытащить базу данныз и отобразить на лицевой странице

from app.models import Trailer
from app.models import Truck
trailers = [
    Trailer(license_plate="AA1237BB"),
    Trailer(license_plate="AA1238BB"),
    Trailer(license_plate="AA1239BB"),
]
for t in trailers:
    db.session.add(t)
db.session.commit()

truck = [
    Truck(license_plate="BI4078BB"),
    Truck(license_plate="BI8576BB"),
    Truck(license_plate="BI7185BB"),
]
for p in truck:
    db.session.add(p)
db.session.commit()