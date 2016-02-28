#!/usr/bin/python -tt
import os
from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from table_def import Contact

# Get path of script
path = os.path.dirname(os.path.abspath(__file__))

class SQL(object):
  """Represents a SQL object. The object is used to insert new contacts into the rolodex.
  """

  def __init__(self):
    """Returns a SQL object"""
    self.engine = create_engine('sqlite:///{0}/rolodex.db'.format(path))
    self.Session = sessionmaker(bind=self.engine)
    self.session = self.Session()
    
  def add_contact(self, phone_number, sms_address):
    """Adds contact to the database"""
    try:
      new_contact = Contact(phone_number, sms_address)
      self.session.add(new_contact)
      self.session.commit()
    except exc.IntegrityError:
       self.session.rollback()
       print "[-] Error adding contact!"      
    
  def delete_contact(self, phone_number):
    """Deletes contact to the database"""
    try:
      res = self.session.query(Contact).filter(Contact.phone_number==phone_number).first()
      self.session.delete(res)
      self.session.commit()
    except:
       self.session.rollback()
       print "[-] Error removing contact!"

  def valid_contact(self, phone_number):
    """Returns if contact information is the database"""
    try:
      res = self.session.query(Contact).filter(Contact.phone_number==phone_number).first()
      if res.phone_number:
        return True
      else:
        return False
    except:
      print "[-] No contact found!"
      return False


  def get_contact(self, phone_number):
    """Returns one contact information from the database"""
    try:
      res = self.session.query(Contact).filter(Contact.phone_number==phone_number).first()
      return res
    except:
      print "[-] No contact found!"
      return False

  def get_contacts(self):
    """Returns list of contacts information from the database"""
    try:
      contacts = []
      res = self.session.query(Contact).all()
      for contact in res:
        contacts.append(contact)
      return contacts
    except:
      print "[-] No contacts found!"
      return False

    