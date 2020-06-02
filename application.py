from flask import Flask
from flask_restful import Api
import datetime
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.secret_key = 'raju'
api = Api(application)

@app.before_first_request
def create_tables():
    db.create_all()

# config JWT to expire within half an hour
application.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)

jwt = JWT(application, authenticate, identity)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(application)
    application.run(port=5000)
