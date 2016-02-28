#!/usr/bin/python -tt
import os
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# Get path of script
path = os.path.dirname(os.path.abspath(__file__)) 
engine = create_engine('sqlite:///{0}/rolodex.db'.format(path))
Base = declarative_base()
 
class Contact(Base):
    """"""
    __tablename__ = "contacts"
 
    id = Column(Integer, primary_key=True)
    phone_number = Column(String, unique=True)
    sms_address = Column(String, unique=True)

    def __init__(self, phone_number, sms_address):
        """"""
        self.phone_number = phone_number
        self.sms_address = sms_address    
 
# create table
Base.metadata.create_all(engine)