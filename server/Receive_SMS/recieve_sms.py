import time
import datetime
import urllib2, urllib
from dateutil import tz
from twilio.rest import TwilioRestClient
from sql.sql import SQL
from lib.otp import OTP

def main():
  from firebase import firebase
  """
  Main function that runs on program execution. 
  """
  # Account Sid and Auth Token from twilio.com/user/account
  account_sid = "AC5814966080955f9eea155e9f3b3458b7"
  auth_token  = "f905a34ad6ede29ec27d19a398231b9d"
  client = TwilioRestClient(account_sid, auth_token)
  firebase = firebase.FirebaseApplication('https://popping-fire-3662.firebaseio.com', None)
  from_zone = tz.gettz('UTC')
  to_zone = tz.gettz('America/Chicago')
  sql = SQL()
  otp = OTP()
 
  while True:
    # Get the messages from 
    messages = client.messages.list()

    for message in messages:
      if not sql.exist_in_queue(message.sid):
        if not message.body == '':
          try:
            date_sent = message.date_sent.replace(tzinfo=from_zone)
            central = date_sent.astimezone(to_zone)

            message_date = central.strftime("%Y-%m-%d")
            message_time = central.strftime("%H:%M:%S")

            phone_number = message.from_[2:]

            sql.add_queue(message.sid, message.body, message.from_, message_date, message_time)
            new_queue = {'date': message_date, 'time': message_time, 'body': message.body, 'phone' : message.from_, 'acct_name': 'Ryan'}
            result = firebase.post('/admins', new_queue, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
            print result

            value = otp.encrypt('{"phone_number": "%s", "message": "Thank you for using csgi support. We received your message your estimated wait time for a return call is 22 minutes."}' % (phone_number))

            url = 'http://localhost:8080/api/send?value={0}'.format(value)
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            print response.read()
          except:
            print '[-] Error sending message trying again'

    
    time.sleep(1)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
