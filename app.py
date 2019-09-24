from flask import Flask, jsonify
from config import db_config 
from flask_restful import Resource, Api
from resources.generator_url import Url
from db import db 

app = Flask(__name__)
api = Api( app )
db.init_app( app )

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Url, '/')


if __name__ == '__main__':
    app.run(debug=True)  
