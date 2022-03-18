from app import myapp
from flask import flash, redirect, render_template
from app.forms import CityForm

@myapp.route('/', methods=['GET', 'POST'])
def home():
    name = 'Aaron'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    form = CityForm()
    if form.validate_on_submit():
        flash(form.new_city.data)
        return redirect('/')
    return render_template('home.html', name=name, city_names=city_names, form=form)