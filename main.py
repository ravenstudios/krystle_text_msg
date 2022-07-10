# to start app run "uvicorn main:app --reload"
from fastapi import FastAPI
import random
from messages import messages
import os
from twilio.rest import Client

app = FastAPI()

account_sid = 'ACd99a2e85a75181fc14af87e02e1aee05'
auth_token = '74e03441f0fc920769cdb4ae6c127e63'
client = Client(account_sid, auth_token)


@app.get("/")
async def root():
    msg = messages[random.randint(0, len(messages))]

    message = client.messages \
                    .create(
                         body=msg,
                         from_='+18593281744',
                         to='+12544622979'
                     )
    return {"message": message.sid}
    
