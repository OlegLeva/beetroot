from flask import Flask, render_template, flash, redirect, url_for
from a_notes.app.forms import LoginForm, AddDoc
from a_notes.create_DB_SQL import add_car_list, get_all_auto_trains
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'password'


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Oleh'}
    auto_train_home = get_all_auto_trains()
    # here will be a list of all auto trains
    return render_template('index.html', auto_train_home=auto_train_home, user=user)


@app.route('/add_document', methods=['GET', 'POST'])
def add_document():
    # add document and link it to truck/driver/trailer
    form = AddDoc()
    if form.validate_on_submit():
        add_car_list()
        flash('Enter data {}'.format(form.add_document.data))
    return render_template('add_doc.html', form=form)


'''Todo: home, add_doc, truck_doc, driver_doc, trailer_doc'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
