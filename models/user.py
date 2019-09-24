from db import db
import datetime 
from sqlalchemy import Column, Integer, DateTime, Text, String


class UserModel(db.Model):
    __tablename__ = "user"
    __table_args__ = { "schema": "mini_url" }

    id_user = Column( Integer, primary_key = True )
    email = Column( String( 200 ), unique=True )
    password = Column( Text, nullable=False )
    create_at = Column( DateTime, default=datetime.datetime.utcnow )
    
    def __init__( self, email, password ):
        self.email = email
        self.password = password

    def save_user( self ):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    
    
    
