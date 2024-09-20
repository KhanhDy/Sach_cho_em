from flask import Flask, jsonify, url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from cart_option import CartOption
from user_option import User_option 
from product import Prod, Product
from db import db
from route.home import home
from route.cart_route import cart_route
from route.account_route import acc_route
from route.product_route import product_route
from os import path

def create_app():
    app = Flask(__name__)
    
    # app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:0123456789@localhost/sce_db?charset=utf8mb4'
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///user.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
 
    app.config['cartOption'] = CartOption(db=db)
    app.config['AccOption'] = User_option(db=db)
    app.config['Prod'] = Prod(db=db)
    app.register_blueprint(cart_route)
    app.register_blueprint(home)
    app.register_blueprint(acc_route)
    app.register_blueprint(product_route)

    return app


if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        db.create_all()
    CORS(app)

    app.run(debug= True, port= 5000)