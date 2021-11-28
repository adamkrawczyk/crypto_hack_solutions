#! /usr/bin/python3 
from Crypto.PublicKey import RSA
from base64 import b64decode

f = open('privacy_enhanced_mail.pem','r')
key = RSA.importKey(f.read())
print(key.d)


