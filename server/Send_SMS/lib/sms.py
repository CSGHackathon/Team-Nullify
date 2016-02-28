#!/usr/bin/python -tt
import base64
import json
import logging
import re 
import smtplib
import urllib2

class SMS(object):
  """Represents a SMS object. The object is used to lookup the mobile provider and send 
  a sms message to the phone number passed into the object.
  """

  @staticmethod
  def setup_log():
    """Returns a logger interface that can be used for any code that uses the SMS object"""
    logger = logging.getLogger('SMS Error')
    hdlr = logging.FileHandler('/var/Send_SMS/sms_error.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.WARNING)
    return logger

  def __init__(self, api_user, api_password):
    """Returns a SMS object with the api username, password, and error logging set"""
    self.api_user = api_user
    self.api_password = api_password
    self.smtp_user = ''
    self.smtp_password = ''
    self.error_log = self.setup_log()

  def _parse_phone_info(self, phone_info):
    """Parses phone information and returns the correct sms gateway address to send a text message"""
    # Get the carrier name
    carrier = phone_info['carrier']['name']

    # Get the phone number
    phone_number = phone_info['query_number']

    # Return the smtp address of the phone number that you want to text
    if re.search('Verizon', carrier, re.IGNORECASE):
      return "%s@vtext.com" % (phone_number)
    elif re.search('Sprint', carrier, re.IGNORECASE):
      return "%s@messaging.sprintpcs.com" % (phone_number)
    elif re.search('T-Mobile', carrier, re.IGNORECASE):
      return "%s@tmomail.net" % (phone_number)
    elif re.search('AT&T', carrier, re.IGNORECASE):
      return "%s@txt.att.net" % (phone_number)
    elif re.search('Alltel', carrier, re.IGNORECASE):
      return "%s@message.alltel.com" % (phone_number)
    elif re.search('Boost', carrier, re.IGNORECASE):
      return "%s@myboostmobile.com" % (phone_number) 
    elif re.search('Virgin', carrier, re.IGNORECASE):
      return "%s@vmobl.com" % (phone_number)
    elif re.search('Cellular', carrier, re.IGNORECASE):
      return "%s@email.uscc.net" % (phone_number)
    else:
      print "[-] Error phone carrier not found. Please check the error log for more details"
      self.error_log.error('Phone carrier not found: %s' % carrier)

  def _is_mobile(self, phone_info):
    """Verifies the phone number is for a mobile device"""
    if phone_info['carrier']['type'] == 'mobile':
      return True
    else:
      return False

  def _get_api_info(self, phone_number):
    """Gets the phone information from the twilio api"""
    # Get the data from the twilio api
    try:
      request = urllib2.Request("https://lookups.twilio.com/v1/PhoneNumbers/%s?Type=carrier" % phone_number)
      base64string = base64.encodestring('%s:%s' % (self.api_user, self.api_password)).replace('\n', '')
      request.add_header("Authorization", "Basic %s" % base64string)   
      result = urllib2.urlopen(request)
      response = result.read()
    except urllib2.HTTPError:
      print "[-] Error phone number not found. Please check the error log for more details"
      self.error_log.error('Phone number not found: %s' % phone_number)
      return False

    # Load the twilio api into a python dictionary
    phone_info = json.loads(response)

    # Add the 10 digit number that was passed in
    phone_info['query_number'] = phone_number

    # If the phone is a mobile phone number store the phone information
    if self._is_mobile(phone_info):
      return self._parse_phone_info(phone_info)
    else:
      print "[-] Error phone number was not a mobile device. Please check the error log for more details"
      self.error_log.error('Error phone number was not a mobile device: %s' % phone_number)
      return False

  def get_sms_address(self, phone_number):
    """Sends a sms message to the phone number that was input, returns true on success and false on failure"""
    try:
      # Use the twilio to get the phone number and provider
      return self._get_api_info(phone_number)  
    except:
      print "[-] Error SMS address could not be found. Please check the error log for more details"
      self.error_log.error('Error SMS address could not be found for phone_number: %s' % phone_number)
      return False

  def send_message(self, sms_address, message):
    """Sends a sms message to the phone number that was input, returns true on success and false on failure"""
    try:     
      # Establish a secure session with gmail's outgoing SMTP server using your gmail account
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

      # Login to gmail's smtp server
      server.login('hackathonemail@gmail.com', 'AppleSucks99')

      # Send text message through SMS gateway of destination number
      server.sendmail('support@csgi.com', sms_address, message )

      # If we get to this point then everything worked
      return True
    except:
      print "[-] Error message not sent. Please check the error log for more details"
      self.error_log.error('Error message not sent to phone_number: %s' % phone_number)
      return False