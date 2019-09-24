from flask_restful import Resource
from models.url import UrlModel
from flask import redirect
from flask_jwt_extended import  jwt_required, get_jwt_identity
import json


def map_list_json( url ):
    print(url.to_json() )
    return url.to_json()

class AllUrls( Resource ):
    @jwt_required
    def get(self):   
        current_user = get_jwt_identity() 
        urls_list = UrlModel.get_by_user( current_user['id'] )
        urls = [i.to_json() for i in urls_list]
        return {
            'message' : 'Ok',
            'status_code' : 200,
            'data' :  urls
        }
     