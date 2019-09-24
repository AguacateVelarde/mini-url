from flask_restful import Resource, Api, reqparse
from models.user import UserModel 
from flask import Flask, jsonify
from db import db 
import bcrypt
from flask_jwt_extended import create_access_token
import datetime

class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, help="Email is necessary")
        parser.add_argument('password', required=True, help="Password is necessary")
        args = parser.parse_args()
        email = args['email']
        password = bcrypt.hashpw(args['password'].encode('utf8'), bcrypt.gensalt())
        
        user = UserModel( email, password )
        verifyUser = UserModel.get_by_email( email )
        
        if( verifyUser is not None ):
           return {
               'message' : 'Email ya registrado',
               'status_code' : 400
           }, 400
           
        user.save() 
        expires = datetime.timedelta(days=15)
        access_token = create_access_token(identity=user.to_json(), expires_delta=expires)
           
        return {
            "message" : 'Ok',
            "status_code" : 200,
            "token": access_token
        }, 200
   
class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, help="Email is necessary")
        parser.add_argument('password', required=True, help="Password is necessary")
        args = parser.parse_args()
        email = args['email']
        
        temporal_user = UserModel.get_by_email( email )
        if temporal_user is None: 
            return {
               'message' : 'Email no encontrado',
               'status_code' : 400
            }, 400
       
        if bcrypt.checkpw( args['password'].encode('utf8'), temporal_user.password ) is False :
            return {
               'message' : 'Contraseña incorrecta',
               'status_code' : 400
            }, 400
        expires = datetime.timedelta(days=15)
        access_token = create_access_token(identity=temporal_user.to_json(), expires_delta=expires)
        return {
            "message" : 'Ok',
            "status_code" : 200,
            "token": access_token
        }, 200