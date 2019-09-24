import os
import sys
import unittest
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
from db import db
import json

class UrlAllTest(unittest.TestCase):
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
    
    def get_token(self):
        login_response = self.app.post(
            '/user/login', 
            data=dict(email="lg.velarde.andrade@gmail.com", password="edison"),
            follow_redirects=False)
        return json.loads(login_response.data)['token']  
    
    def test_all_urls_ok( self ):
        token = self.get_token()
        response = self.app.get(
            '/url/all', 
            headers={"Authorization": "Bearer {}".format(token)},
            follow_redirects=False
        )
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( json.loads( response.data )['message'], 'Ok')
        self.assertTrue( isinstance(json.loads( response.data )['data'], list) )
        
    def test_all_urls_notsend_auth( self ):
        response = self.app.get(
            '/url/all',             
            follow_redirects=False
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual( json.loads(response.data)['msg'], 'Missing Authorization Header' )
        
        
    def get_all_urls( self ):
        token = self.get_token()
        response = self.app.get(
            '/url/all', 
            headers={"Authorization": "Bearer {}".format(token)},
            follow_redirects=False
        )
        return json.loads( response.data )['data']
        
    def test_url_redirect( self ):
        urls = self.get_all_urls()
        url_test = 'u/{}'.format( urls[0]['shorted_id'] )
        response = self.app.get(
            url_test,             
            follow_redirects=False
        )
        self.assertEqual( response.status_code, 302 )
        self.assertEqual( response.location, urls[0]['url'] )
        
if __name__ == "__main__":
    unittest.main()