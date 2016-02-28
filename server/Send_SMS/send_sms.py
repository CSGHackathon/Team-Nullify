#!/usr/bin/python -tt
import tornado.ioloop
import tornado.web
import re
from tornado.options import parse_command_line, define, options
from lib.sms import SMS
from lib.otp import OTP
from sql.sql import SQL

class SendHandler(tornado.web.RequestHandler):
  def set_default_headers(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Methods", "GET")

  def get(self):
    sms = SMS(api_user='AC5814966080955f9eea155e9f3b3458b7', api_password='f905a34ad6ede29ec27d19a398231b9d')
    otp = OTP()
    db = SQL()

    # Get the value parameter and attempt to decrypt it
    value = self.get_argument("value")
    jsonDict = otp.decrypt(value)

    # Make sure the phone_number and message decrypted correctly
    if jsonDict and jsonDict['phone_number'] and jsonDict['message']:
      phone_number = jsonDict['phone_number']
      message = jsonDict['message']

      # Validate the phone number
      if re.match('^\d{10}$', phone_number):
        #Check if the phone number is already in the database, if not add the number to the database and send the message
        if db.valid_contact(phone_number):
          contact = db.get_contact(phone_number)
          if sms.send_message(contact.sms_address, message):
            self.write({'status': 'success', 'message': ''})
          else:
            self.write({'status': 'error', 'message': 'SMS could not be sent!'})
        else:
          sms_address = sms.get_sms_address(phone_number)
          if sms_address:
            db.add_contact(phone_number, sms_address)
            if sms.send_message(sms_address, message):
              self.write({'status': 'success', 'message': ''})
            else:
              self.write({'status': 'error', 'message': 'SMS could not be sent!'})
          else:
            self.write({'status': 'error', 'message': 'Could not find sms gateway!'})
      else:
        self.write({'status': 'error', 'message': 'Invalid phone number format must be 10 digits only ex. (1112223333)'})
    else:
      self.write({'status': 'error', 'message': 'Malformed Input Data'})

class SendAllHandler(tornado.web.RequestHandler):
  def set_default_headers(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Methods", "GET")

  def get(self):
    sms = SMS(api_user='AC5814966080955f9eea155e9f3b3458b7', api_password='f905a34ad6ede29ec27d19a398231b9d')
    otp = OTP()
    db = SQL()

    # Get the value parameter and attempt to decrypt it
    value = self.get_argument("value")
    jsonDict = otp.decrypt(value)

    # Make sure the phone_number and message decrypted correctly
    if jsonDict and jsonDict['message']:
      message = jsonDict['message']
      # Send the message to everyone in the database
      contacts = db.get_contacts()
      for contact in contacts:
        if sms.send_message(contact.sms_address, message):
          self.write({'status': 'success', 'message': ''})
        else:
          self.write({'status': 'error', 'message': 'SMS could not be sent!'})
    else:
      self.write({'status': 'error', 'message': 'Malformed Input Data'})

class AddHandler(tornado.web.RequestHandler):
  def set_default_headers(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Methods", "GET")

  def get(self):
    otp = OTP()
    db = SQL()

    # Get the value parameter and attempt to decrypt it
    value = self.get_argument("value")
    jsonDict = otp.decrypt(value)

    # Make sure the phone_number and message decrypted correctly
    if jsonDict and jsonDict['phone_number']:
      # Validate the phone number
      if re.match('^\d{10}$', phone_number):
        # Get the sms address of the phone number and add that to the database
        sms_address = sms.get_sms_address(phone_number)
        if sms_address:
          db.add_contact(phone_number, sms_address)
        else:
          self.write({'status': 'error', 'message': 'Could not find sms gateway!'})
      else:
        self.write({'status': 'error', 'message': 'Invalid phone number format must be 10 digits only ex. (1112223333)'})
    else:
      self.write({'status': 'error', 'message': 'Malformed Input Data'})

handlers = [
    (r"/api/send", SendHandler),
    (r"/api/add", AddHandler),
    (r"/api/send/all", SendAllHandler),
]

if __name__ == "__main__":
    parse_command_line()
    
    application = tornado.web.Application(handlers)
    application.listen(8080)
    
    tornado.ioloop.IOLoop.instance().start()
