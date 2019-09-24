from db import db
import datetime 
from sqlalchemy import Column, Integer, DateTime, Text, String
from passlib.hash import pbkdf2_sha256 as sha256



class UrlModel(db.Model):
    __tablename__ = "url"
    #__table_args__ = { "schema": "mini_url" }
    
    id_url  = Column( Integer, primary_key = True )
    id_user = Column( Integer )
    real_url = Column( Text )
    shorted_id = Column( Text )
    
    def __init__( self, id_user, real_url,shorted_id  ):
        self.id_user = id_user
        self.real_url = real_url 
        self.shorted_id = shorted_id

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_by_shorted(shorted_id):
        return UrlModel.query.filter_by(shorted_id=shorted_id).first()
    
    @staticmethod
    def get_by_user(id_user):
        return UrlModel.query.filter_by(id_user=id_user).all()
    
    
    def __repr__(self):
        return '< URL : {}, {}, {}>'.format(self.id_user, self.real_url, self.shorted_id)
    
    def to_json( self ):
        return {
            'url' : self.real_url,
            'shorted_id' : self.shorted_id
        }
        
    def get_url( self ):
        return 'http://localhost:500/u/' + self.shorted_id
    
    def get_real_url( self ):
        return self.real_url