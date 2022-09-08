from flask_app import app
from flask import Flask, render_template, request, redirect, session 
from flask_app.models.cookie import Cookie


@app.route('/cookies') #this is to show ALL orders (also home)
def route():
    all_orders = Cookie.get_all()
    return render_template('read_all.html', all_the_orders = all_orders)

@app.route('/cookies/new') #this is the page/form to add a new order
def user():
    return render_template('create.html')

@app.route('/new/order', methods = ["POST"]) #this is actually adding the new order
def create_order():
    print(request.form)
    if not Cookie.validate_create(request.form): #this is validating info
        return redirect ('/cookies/new')
    data = {
        'customer_name': request.form['customer_name'],
        'cookie_type': request.form['cookie_type'],
        'amount': request.form['amount']
    }
    show_user = Cookie.create(data)
    return redirect('/cookies')

@app.route('/cookies/edit/<int:id>') #this is the page/form to edit an order
def update(id):
    data = {
        'id' : id
    }
    a_order = Cookie.get_one(data)
    return render_template('edit.html', one_order = a_order)

@app.route('/edit/<int:id>', methods = ["POST"]) #this is actually adding the new order
def edit_order(id):
    print(request.form)
    if not Cookie.validate_create(request.form): #this is validating info
        return redirect (f'/cookies/edit/{id}')
    data = {
        'id' : id,
        'customer_name': request.form['customer_name'],
        'cookie_type': request.form['cookie_type'],
        'amount': request.form['amount']
    }
    Cookie.update(data)
    return redirect('/cookies')