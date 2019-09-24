import os
import sys
import unittest
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
from db import db
import json

class UrlTest(unittest.TestCase):
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

    def test_url_failure_post(self):
        response = self.app.post('/url', follow_redirects=False)
        self.assertEqual(response.status_code, 401)
        self.assertEqual( json.loads(response.data)['msg'], 'Missing Authorization Header' )
        
    def test_url_ok(self):
        token = self.get_token()
        response = self.app.post('/url', 
                                data=dict(url="http://google.com"),
                                headers={"Authorization": "Bearer {}".format(token)},
                                follow_redirects=False)
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( json.loads( response.data )['message'], 'Ok')
        self.assertTrue( json.loads( response.data )['shorted'] )
        self.assertEqual( json.loads( response.data )['url'], 'http://google.com')
        
    
    def test_url_notsend_url(self):
        token = self.get_token()
        response = self.app.post('/url', 
                                data=dict(),
                                headers={"Authorization": "Bearer {}".format(token)},
                                follow_redirects=False)
        self.assertEqual( response.status_code, 400 )
        self.assertEqual( json.loads( response.data )['message']['url'],  "Url is necessary")
        
        
      
    def get_token(self):
        login_response = self.app.post(
            '/user/login', 
            data=dict(email="lg.velarde.andrade@gmail.com", password="edison"),
            follow_redirects=False)
        return json.loads(login_response.data)['token']  
    
if __name__ == "__main__":
    unittest.main()