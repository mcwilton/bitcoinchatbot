import requests
import os
from twilio.rest import Client


elif 'qr code' in incoming_msg:
        	bit_address = incoming_msg.split()[2]
        	qr_code_url = f'https://www.bitcoinqrcodemaker.com/api/?style=bitcoin&address={bit_address}'
        	msg.body("Here's your Bitcoin QR Code Image!")
        	msg.media(qr_code_url)
        	responded=True


        	

def reply_whatsapp():

    response = MessagingResponse()
    num_media = int(request.values.get("NumMedia"))
    if not num_media:
        msg = response.message("Send us an image!")
    else:
        msg = response.message("Thanks for the image. Here's one for you!")
        msg.media(GOOD_BOY_URL)
    return str(response)



account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+14155238886',
         body="It's taco time!",
         to='whatsapp:+15017122661'
     )

print(message.sid)

qr_code_url = 'https://www.bitcoinqrcodemaker.com/api/?style=bitcoin&address=1M5m1DuGw4Wyq1Nf8sfoKRM6uA4oREzpCX'
#incoming_msg == 'dog':
# return a dog pic
r = requests.get('https://www.bitcoinqrcodemaker.com/api/?style=bitcoin&address=1M5m1DuGw4Wyq1Nf8sfoKRM6uA4oREzpCX')
data = r
msg = response.message("Thanks for the image. Here's one for you!")
msg.media(GOOD_BOY_URL)
#print(r)
#print(data)
#msg.media(data['message'])





