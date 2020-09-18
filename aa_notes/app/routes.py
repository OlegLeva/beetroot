from app import app, db
from app.forms import AddDoc, AddTrain
from app.models import AutoTrain, Truck, Trailer, Driver
from flask import render_template, flash, redirect, request

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    autotrains = AutoTrain.query.all()
    form = AddTrain()
    return render_template('index.html', autotrains=autotrains, form=form)


@app.route('/add_train', methods=['GET', 'POST'])
def add_train():
    truck_lp = request.form['truck_id']
    truck = Truck(truck_lp)
    db.session.add(truck)
    db.session.commit()
    trailer_lp = request.form['trailer_id']
    trailer = Trailer(trailer_lp)
    db.session.add(trailer)
    db.session.commit()
    driver_lp = request.form['driver_id']
    driver = Driver(driver_lp)
    db.session.add(driver)
    db.session.commit()
    return redirect("/index")




@app.route('/add_document', methods=['GET', 'POST'])
def add_document():
    # add document and link it to truck/driver/trailer
    form = AddDoc()
    if form.validate_on_submit():
        flash('Enter data {}'.format(form.add_document.data))
    return render_template('add_data.html', form=form)

