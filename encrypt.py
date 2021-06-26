import rsa
import rsa.randnum
import random
from Crypto.Cipher import AES
from secrets import token_bytes

def encrypt(msg,key): #Sending End
    cipher = AES.new(key,AES.MODE_EAX) #Using the Random Key, encrypt the data using AES
    nonce = cipher.nonce
    ciphertext,tag = cipher.encrypt_and_digest(msg.encode('ascii')) #Encode the Data to ASCII, since AES takes only Bytes
    return nonce, ciphertext, tag
