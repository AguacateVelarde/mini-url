from db import db
import datetime 
from sqlalchemy import Column, Integer, DateTime, Text, String
from passlib.hash import pbkdf2_sha256 as sha256

 
class UserModel(db.Model):
    __tablename__ = "user"
    #__table_args__ = { "schema": "mini_url" }

    id_user = Column( Integer, primary_key = True )
    email = Column( String( 200 ), unique=True )
    password = Column( Text, nullable=False )
    create_at = Column( DateTime, default=datetime.datetime.utcnow )
    
    def __init__( self, email, password ):
        self.email = email
        self.password  = password
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_by_id(id):
        return UserModel.query.get(id)

    @staticmethod
    def get_by_email(email):
        return UserModel.query.filter_by(email=email).first()

    def __repr__(self):
        return '<{}, {}>'.format(self.email, self.password)

    def to_json(self):
        return{
            "email" : self.email,
            "id" : self.id_user
        }
    
    def get_password(self):
        return self.password
    
    
    
