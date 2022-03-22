from app import myobj
from flask import flash, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CityForm(FlaskForm):
    new_city = StringField('City Name')
    submit = SubmitField('Submit')

name = 'Aaron'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route('/', methods=['GET', 'POST'])
def home():
    form = CityForm()
    if form.validate_on_submit():
        flash(form.new_city.data)
        return redirect('/')
    return render_template('home.html', name=name, city_names=city_names, form=form)