from flask import Flask, render_template, flash, redirect, url_for
from a_notes.app.forms import LoginForm
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
    user = {'username': 'Oleg'}
    car_list = [
        {
            'car_id': 1,
            'car_numb': 'BI4078CE',
            'trailer_numb': 'BI2324XK',
            'driver': 'Tereshchenko Dmitro'
        }
    ]
    return render_template('index.html', title='Home', user=user, car_list=car_list)


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
