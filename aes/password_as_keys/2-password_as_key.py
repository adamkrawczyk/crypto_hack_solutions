#!/usr/bin/python3
from Crypto.Cipher import AES
import hashlib
import random

# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("/home/adam/projects/github/crypto_hack/aes/password_as_keys/dictionary_words") as f:
    words = [w.strip() for w in f.readlines()]

ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

def decrypt(ciphertext, KEY):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}



for w in words:
    keyword = w
    KEY = hashlib.md5(keyword.encode()).digest()
    tmp = decrypt(ciphertext, KEY)['plaintext']
    if "63727970746f7b" in tmp: #63727970746f7b crypto
        print(keyword)
        print(tmp)
        print(KEY)
        print(bytes.fromhex(KEY).decode('utf-8'))
    