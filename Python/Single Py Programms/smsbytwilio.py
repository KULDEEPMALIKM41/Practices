
from twilio.rest import Client
accountSid ='ACeab4502f63d317fbc0aceb0fc6e4049d'
authToken ='44ad35c0a8cf38d83cf8669e0fde4fa5'
client = Client(accountSid,authToken)
myTwilioNumber ='+17067444143'
destCellPhone ='+918818919146'
myMessage = client.messages.create(body = "whatever", from_=myTwilioNumber, to=destCellPhone)