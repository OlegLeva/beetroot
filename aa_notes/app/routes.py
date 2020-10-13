from app import app, db
from app.forms import AddTrain
from app.models import AutoTrain, Truck, Trailer, Driver, Document, Notification
from flask import render_template, redirect, request


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    autotrains = AutoTrain.query.all()
    get_phone = Driver.query.all()

    form = AddTrain()
    return render_template('index.html', autotrains=autotrains, get_phone=get_phone, form=form)


@app.route('/index/<int:id>')
def edit1(id):
    autotrain = AutoTrain.query.get(id)

    return render_template('edit1.html', autotrain=autotrain)


@app.route('/index/<int:id>/del')
def delete(id):
    autotrain = AutoTrain.query.get_or_404(id)

    db.session.delete(autotrain)
    db.session.commit()

    return redirect("/index")


# NEW FORM
@app.route('/add_autotrain', methods=['GET', 'POST'])
def add_autotrain():
    if request.method == 'POST':
        train = AutoTrain(id=request.form['id_autotrain'],
                          truck_id=request.form['truck_license_plate'],
                          trailer_id=request.form['trailer_license_plate'],
                          driver_id=request.form['driver_name'])
        truck = Truck(license_plate=train.truck_id)
        trailer = Trailer(license_plate1=train.trailer_id)
        driver = Driver(id=train.driver_id, phone=request.form['phone'])

        db.session.add(truck)
        db.session.add(trailer)
        db.session.add(driver)
        db.session.add(train)
        db.session.commit()

        return render_template("/add_autotrain.html")


@app.route('/add_train', methods=['GET', 'POST'])
def add_train():
    truck = Truck(license_plate=request.form['truck_license_plate'])
    trailer = Trailer(license_plate1=request.form['trailer_license_plate'])
    driver = Driver(id=request.form['driver_name'])
    train = AutoTrain(id=request.form['id_autotrain'],
                      truck_id=truck.license_plate,
                      trailer_id=trailer.license_plate1,
                      driver_id=driver.id,
                      phone_id=request.form['phone'])
    try:
        db.session.add(truck)
        db.session.add(trailer)
        db.session.add(driver)
        db.session.add(train)
        db.session.commit()

        return redirect("/index")
    except:
        return redirect("/index")


@app.route('/add_doc_truck', methods=['GET', 'POST'])
def add_doc_truck():
    if request.method == 'POST':
        name = request.form['name']
        exp_date = request.form['exp_date']
        truck_id = request.form['truck_id']
        document = Document(name=name, exp_date=exp_date, truck_id=truck_id)

        # days_before = request.form['days_before']
        # notified = Notification(id=Document.query.filter_by(name='name').first().id, days_before=days_before)

        try:
            db.session.add(document)
            # db.session.add(notified)
            db.session.commit()

            return render_template('add_doc_truck.html')
        except:
            return 'Введены неверные данные'
    else:
        return render_template('add_doc_truck.html')


@app.route('/add_doc_trailer', methods=['GET', 'POST'])
def add_doc_trailer():
    if request.method == 'POST':
        name = request.form['name']
        exp_date = request.form['exp_date']
        trailer_id = request.form['trailer_id']

        document = Document(name=name, exp_date=exp_date, trailer_id=trailer_id)

        try:
            db.session.add(document)
            db.session.commit()
            return render_template('add_doc_trailer.html')
        except:
            return 'Введены неверные данные'
    else:
        return render_template('add_doc_trailer.html')


@app.route('/add_doc_driver', methods=['GET', 'POST'])
def add_doc_driver():
    if request.method == 'POST':
        name = request.form['name']
        exp_date = request.form['exp_date']
        driver_id = request.form['driver_id']

        document = Document(name=name, exp_date=exp_date, driver_id=driver_id)

        try:
            db.session.add(document)
            db.session.commit()
            return render_template('add_doc_driver.html')
        except:
            return 'Введены неверные данные'
    else:
        return render_template('add_doc_driver.html')
