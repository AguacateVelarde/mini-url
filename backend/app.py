from flask import Flask, jsonify
from config import db_config , jwt_secret_key
from flask_restful import Resource, Api
from resources.generator_url import Url
from resources.url_catch import SendUrl
from resources.user import Login, Register
from resources.list_all_urls import AllUrls
from db import db 
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api( app )
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = jwt_secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = db_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app( app )
jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Url, '/url')
api.add_resource(SendUrl, '/u/<url>', )
api.add_resource(Login, '/user/login')
api.add_resource(Register, '/user/register')
api.add_resource(AllUrls, '/url/all')


if __name__ == '__main__':
    app.run(debug=True)  
