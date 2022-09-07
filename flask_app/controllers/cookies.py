from flask_app import app
from flask import Flask, render_template, request, redirect, session 
from flask_app.models.cookie import Cookie


@app.route('/cookies') #this is to show ALL orders (also home)
def route():
    all_orders = Cookie.get_all()
    return render_template('read_all.html', all_the_orders = all_orders)