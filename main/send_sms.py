# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
# Find these values at https://twilio.com/user/account
account_sid = "ACf439934e990cf1ee177f7d697ff4d542"
auth_token = "7da9c848dbb0bf7b99050f7e46b261dc"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(to="+37455433423", from_="+16466062534",
body="Hello Erevan!")
