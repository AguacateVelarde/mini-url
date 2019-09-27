import os
import sys
import unittest
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
from db import db
import uuid

class LoginRegisterTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['JWT_SECRET_KEY'] = 'efvbuyy4y86qu4yg'
        self.app = app.test_client()       
        self.assertEqual(app.debug, False)
        db.init_app( app )        
    
    def tearDown(self):
        pass
    
    def test_register_ok( self ):
        email = 'email{}@gmail.com'.format(uuid.uuid1())
        response = self.app.post(
            '/user/register',
            data=dict(email=email, password="edison"),
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual( json.loads(response.data)['message'], 'Ok' )
        self.assertTrue( json.loads(response.data)['token'] )
        
    def test_register_error_email_duplicate( self ):
        response = self.app.post(
            '/user/register',
            data=dict(email='lg.velarde.andrade@gmail.com', password="edison"),
            follow_redirects=False
        )
        self.assertEqual( response.status_code, 400 )
        self.assertEqual( json.loads( response.data )['message'], 'Email ya registrado')
      
    def test_register_error_notsend_email( self ):
        response = self.app.post(
            '/user/register', 
            data=dict( password="edison" ),
            follow_redirects=False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual( json.loads( response.data )['message']['email'],  "Email is necessary")
        
    def test_register_error_notsend_password( self ):
        response = self.app.post(
            '/user/register', 
            data=dict( email="lg.velarde.andrade@gmail.com" ),
            follow_redirects=False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual( json.loads( response.data )['message']['password'],  "Password is necessary")
  

    def test_login_ok( self ):
        response = self.app.post(
            '/user/login', 
            data=dict(email="lg.velarde.andrade@gmail.com", password="edison"),
            follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        self.assertEqual( json.loads(response.data)['message'], 'Ok' )
        self.assertTrue( json.loads(response.data)['token'] )
        
    def test_login_error_notsend_email( self ):
        response = self.app.post(
            '/user/login', 
            data=dict( password="edison" ),
            follow_redirects=False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual( json.loads( response.data )['message']['email'],  "Email is necessary")
        
    def test_login_error_notsend_password( self ):
        response = self.app.post(
            '/user/login', 
            data=dict( email="lg.velarde.andrade@gmail.com" ),
            follow_redirects=False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual( json.loads( response.data )['message']['password'],  "Password is necessary")

    def test_login_error_bad_password( self ):
        response = self.app.post(
            '/user/login', 
            data=dict(email="lg.velarde.andrade@gmail.com", password=""),
            follow_redirects=False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual( json.loads(response.data)['message'], 'Contraseña incorrecta' )

    def test_login_error_bad_email( self ):
        response = self.app.post(
            '/user/login', 
            data=dict(email="lg.velarde.andrade@hotmail.com", password="edison"),
            follow_redirects=False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual( json.loads(response.data)['message'], 'Email no encontrado' )


        
if __name__ == "__main__":
    unittest.main()