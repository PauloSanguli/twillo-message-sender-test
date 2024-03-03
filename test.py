#sent messages with twillo free
from twilio.rest import Client

import os
from dotenv import load_dotenv


load_dotenv()

client = Client(
    os.getenv("ACCOUNT_ID"),
    os.getenv("ACCOUNT_TOKEN")
)
msg = client.messages.create(
    to="+244930751560",
    from_=os.getenv("TWILLO_NUMBER"),
    body="hello word from python twillo"
)
print(msg.body)
