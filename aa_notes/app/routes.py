from app import app
from app.forms import AddDoc
from flask import render_template, flash


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Maxim'}
    return render_template('index.html', title='Home', user=user)

@app.route('/add_document', methods=['GET', 'POST'])
def add_document():
    # add document and link it to truck/driver/trailer
    form = AddDoc()
    if form.validate_on_submit():

        flash('Enter data {}'.format(form.add_document.data))
    return render_template('add_data.html', form=form)