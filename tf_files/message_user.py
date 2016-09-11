import time
import os
from twilio.rest import TwilioRestClient

def load_twilio_config():
    twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_number = os.environ.get('TWILIO_NUMBER')
    target_number = os.environ.get('TARGET_NUMBER')
    return (twilio_number, twilio_account_sid, twilio_auth_token)


def message():
    msg = "Parking Maid seen at %s" % (time.time())
    

def send_message(self, msg):
    twilio_phone_number, account_sid, auth_token, agent_phone_number = load_twilio_config()
    client = TwilioRestClient(account_sid, auth_token)
    TwilioService.client.messages.create(to=agent_phone_number,
    from_=twilio_phone_number,
    body=msg)

if __name__ == "__main__":
    send_message()
