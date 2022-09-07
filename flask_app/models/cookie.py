from flask_app.config.mysqlconnection import connectToMySQL

class Cookie:
    def __init__(self,data):
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