from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie:
    def __init__(self,data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod #this is to show all the orders
    def get_all(cls):
        query = 'SELECT * FROM orders;'
        results = connectToMySQL('cookie_orders').query_db(query)
        print(results)
        all_orders = []
        for one_order in results:
            all_orders.append(cls(one_order))
        return all_orders
    
    @classmethod #this is to read one orders info
    def get_one(cls, data):
        query = 'SELECT * FROM orders WHERE id = %(id)s;'
        results = connectToMySQL('cookie_orders').query_db(query, data)
        print(results)
        return cls(results[0])

    
    @classmethod #this is actually adding a new order
    def create(cls, data):
        query = 'INSERT INTO orders (customer_name, cookie_type, amount) VALUES (%(customer_name)s, %(cookie_type)s, %(amount)s);'
        results = connectToMySQL('cookie_orders').query_db(query, data)
        print(results)
        return results
    
    @classmethod #this is to actually edit the order
    def update(cls, data):
        query = 'UPDATE orders set customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, amount = %(amount)s WHERE id = %(id)s;'
        results = connectToMySQL('cookie_orders').query_db(query, data)
        print(results)
        return results
    
    @staticmethod #this is to validate new orders
    def validate_create(reqForm):
        is_valid = True
        if len(reqForm['customer_name']) < 2:
            flash('customer name is too short!')
            is_valid = False
        if len(reqForm['cookie_type']) < 2:
            flash('cookie type is too short!')
            is_valid = False
        if int(reqForm['amount']) < 1: #need to add int for numbers
            flash('must enter at least 1 box')
            is_valid = False
        return is_valid
        #need to add amount
    
    @staticmethod #this is to validate edits 
    def validate_edit(reqForm):
        is_valid = True
        if len(reqForm['customer_name']) < 0:
            flash('must enter customer name!')
            is_valid = False
        if len(reqForm['cookie_type']) < 0:
            flash('must enter cookie type!')
            is_valid = False
        if int(reqForm['amount']) < 1:
            flash('must enter at least 1 box')
            is_valid = False
        return is_valid
        #need to add amount