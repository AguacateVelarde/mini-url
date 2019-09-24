from flask import Flask, jsonify
from config import db_config , jwt_secret_key
from flask_restful import Resource, Api
from resources.generator_url import Url
from resources.user import Login, Register
from db import db 
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api( app )
app.config['JWT_SECRET_KEY'] = jwt_secret_key
db.init_app( app )
jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Url, '/')
api.add_resource(Login, '/user/login')
api.add_resource(Register, '/user/register')


if __name__ == '__main__':
    app.run(debug=True)  
