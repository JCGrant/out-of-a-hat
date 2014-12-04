from flask import render_template, request, flash, redirect, url_for
from out_of_a_hat import app, db
from models import Hat, Item
import re

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        hat_name = request.form['hat_name'].strip()
        made_by = request.form['made_by'].strip()
        item_names = re.split(',\s*\r?\n*', request.form['item_names'].strip())
        
        hat = Hat(hat_name)
        db.session.add(hat)

        for item_name in item_names:
            item = Item(item_name, hat)
            db.session.add(item)

        db.session.commit()

        flash("Your hat was created!")
        
        return redirect(url_for('hat', hat_uuid=hat.uuid))

    return render_template('index.html')

@app.route('/hat/<hat_uuid>')
def hat(hat_uuid):
    hat = Hat.get_by_uuid(hat_uuid)
    return render_template('hat.html', hat=hat)

@app.route('/take_item/<hat_uuid>')
def take_item(hat_uuid):
    hat = Hat.get_by_uuid(hat_uuid)
    item = hat.get_random_item()
    
    if item:
        item_name = item.name
        db.session.delete(item)
        db.session.commit()
    else:
        item_name = "The hat is empty!"

    return render_template('take_item.html', hat=hat, item_name=item_name)
