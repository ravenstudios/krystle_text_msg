# to start app run "uvicorn main:app --reload"
from fastapi import FastAPI
import random
from messages import messages
import os
from twilio.rest import Client

app = FastAPI()

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


@app.get("/get_text_msg")
async def get_text_msg():
    msg = messages[random.randint(0, len(messages))]

    message = client.messages.create(body=msg, from_='+18593281744', to='+12544622979')
    return {"message": message.sid}
    
