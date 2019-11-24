import oauth2 as oauth
import requests
import urllib.parse
import time
from random import getrandbits
import hashlib
import hmac
import base64

#Download all the above packages and zip it into a file and upload to the above lambda function
#this should be zipped along with the Lambda function because AWS is not aware of the required libraries.

def call_oauthurl(event,context):
    message = bytes('BVI~NiVSiHD_RoTJowfq', 'utf-8')
    secret = bytes('Ipro$b2b', 'utf-8')

    signature_base = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())

    signature = urllib.parse.quote(str(signature_base.decode('utf-8')),'')

    print(signature)

    CONSUMER_KEY = 'BVI~NiVSiHD_RoTJowfq'
    CONSUMER_SECRET = 'Ipro$b2b'

    nonce = str(getrandbits(64))

    url = 'https://usdavwip11.infor.com/service/ping?'

    PARAMS = {
            'oauth_consumer_key': CONSUMER_KEY,
            'oauth_signature_method': "HMAC-SHA256",
            'oauth_timestamp': int(time.time()),
            'oauth_nonce': oauth.generate_nonce(),
            'oauth_version': "1.0", 
            'oauth_signature': signature,
            }

    req = oauth.Request(method="get", url='https://usdavwip11.infor.com/service/ping?', parameters=PARAMS)

    #req = oauth.Request(method="POST", url='https://usdavwip11.infor.com/service/ping?', parameters=PARAMS)

    #r = requests.get("https://usdavwip11.infor.com/service/ping?",params=PARAMS)

    #print(r.status_code)
    #print(PARAMS)

    print(dir(req))

    #print(req.url)
    #r = requests.get(url='https://usdavwip11.infor.com/service/ping?', params=PARAMS)

    #print(r)
    return "It was successfull"

print(call_oauthurl())
