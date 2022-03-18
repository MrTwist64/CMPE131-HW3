from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CityForm(FlaskForm):
    new_city = StringField('City Name')
    submit = SubmitField('Submit')