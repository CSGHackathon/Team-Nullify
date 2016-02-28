#!/usr/bin/python -tt
import os
from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from table_def import Queue

# Get path of script
path = os.path.dirname(os.path.abspath(__file__))

class SQL(object):
  """Represents a SQL object. The object is used to insert new contacts into the rolodex.
  """

  def __init__(self):
    """Returns a SQL object"""
    self.engine = create_engine('sqlite:///{0}/queues.db'.format(path))
    self.Session = sessionmaker(bind=self.engine)
    self.session = self.Session()
    
  def add_queue(self, message_sid, message, phone_number, message_date, message_time):
    """Adds contact to the database"""
    try:
      new_queue = Queue(message_sid, message, phone_number, message_date, message_time)
      self.session.add(new_queue)
      self.session.commit()
    except exc.IntegrityError:
       self.session.rollback()
       print "[-] Error adding contact!"      
    
  def exist_in_queue(self, message_sid):
    """Returns if message is in the queue database"""
    try:
      res = self.session.query(Queue).filter(Queue.message_sid==message_sid).first()
      if res.phone_number:
        return True
      else:
        return False
    except:
      return False

  def get_queue(self, message_sid):
    """Returns one queue data information from the database"""
    try:
      res = self.session.query(Queue).filter(Queue.message_sid==message_sid).first()
      return res
    except:
      print "[-] No contact found!"
      return False    