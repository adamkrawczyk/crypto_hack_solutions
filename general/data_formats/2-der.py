#! /usr/bin/python3 
from os import read
from Crypto.PublicKey import RSA
import ssl
from base64 import b64decode

from asn1crypto.x509 import Certificate


with open("2048b-rsa-example-cert.der", "rb") as f:
    cert = Certificate.load(f.read())

data = ssl.DER_cert_to_PEM_cert(cert)
key = RSA.importKey(cert)
print(key.d)


### NOT WORKING :(