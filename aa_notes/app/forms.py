from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddDoc(FlaskForm):
    truck_license_plate = StringField('Enter truck license plate', validators=[DataRequired()])
    trailer_license_plate = StringField('Enter trailer license plate', validators=[DataRequired()])
    driver_name = StringField('Enter driver name', validators=[DataRequired()])
    phone = StringField('Enter phone', validators=[DataRequired()])
    protocol = StringField('Enter the end date of the PROTOCOL', validators=[DataRequired()])
    taxo = StringField('Enter the end date of the TAHO', validators=[DataRequired()])
    msto = StringField('Enter the end date of the MSTO', validators=[DataRequired()])
    ekmt = StringField('Enter the end date of the EKMT', validators=[DataRequired()])
    customs_certificate = StringField('Enter the end date of the Сustoms certificate', validators=[DataRequired()])
