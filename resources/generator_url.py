from flask_restful import Resource, Api

class Url(Resource):
    def get(self):
        return {'hello': 'world'}

    def post( self ):
        return { 'hello':  'from post'} 
