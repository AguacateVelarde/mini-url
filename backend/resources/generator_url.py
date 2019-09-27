from flask_restful import Resource, Api, reqparse, request
from flask_jwt_extended import  jwt_required, get_jwt_identity
import re
from models.url import UrlModel
import uuid 

class Url(Resource):

    @jwt_required
    def post( self ):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, help="Url is necessary")
        args = parser.parse_args()
        url_text = args['url']
        
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url_text)
        
        if len( urls ) == 0:
            return {
                'message' : 'No enviaste una url válida',
                'status_code' : 400
            }, 400
            
        current_user = get_jwt_identity()
        shorted_id = uuid.uuid1().hex
        url = UrlModel( current_user['id'], urls[0], shorted_id  )
        url.save()

        return { 
            'message' : 'Ok',
            'status_code': 200,
            'shorted' : url.get_url(),
            'url': url.real_url
        } 
