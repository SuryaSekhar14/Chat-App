import rsa
import rsa.randnum
import random
from Crypto.Cipher import AES
from secrets import token_bytes
from encrypt import *
from decrypt import *

key = rsa.randnum.read_random_bits(128) #Generate a Random Key
pub_key,prvt_key = rsa.newkeys(512) #Generate Public & Private Keys for RSA Encryption
encrypted_aes_key = rsa.encrypt(key, pub_key) #Encrypt the Random Key using RSA

nonce,ciphertext,tag = encrypt(input("Enter a message: "),key)
plaintext = decrypt(nonce,ciphertext,tag,encrypted_aes_key,prvt_key)
print(f'Cipher text: {ciphertext}')
if not plaintext:
    print('Message is Corrupted')
else:
    print(f'Plain Text: {plaintext}')


