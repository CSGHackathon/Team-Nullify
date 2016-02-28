#!/usr/bin/python -tt
import os
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# Get path of script
path = os.path.dirname(os.path.abspath(__file__)) 
engine = create_engine('sqlite:///{0}/queues.db'.format(path))
Base = declarative_base()
 
class Queue(Base):
    """"""
    __tablename__ = "queues"
 
    id = Column(Integer, primary_key=True)
    message_sid = Column(String, unique=True)
    message = Column(String)
    phone_number = Column(String)
    message_date = Column(String)
    message_time = Column(String)

    def __init__(self, message_sid, message, phone_number, message_date, message_time):
        """"""
        self.message_sid = message_sid
        self.message = message
        self.phone_number = phone_number  
        self.message_date = message_date
        self.message_time = message_time 
 
# create table
Base.metadata.create_all(engine)