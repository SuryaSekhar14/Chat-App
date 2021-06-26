import rsa
import rsa.randnum
import random
from Crypto.Cipher import AES
from secrets import token_bytes

def decrypt(nonce,ciphertext,tag,encrypted_aes_key,prvt_key): #Receiving End
    aes_key = rsa.decrypt(encrypted_aes_key,prvt_key) #Decrypt the Key using RSA
    cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce) #Use the above key to decrypt the Data.
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii') #Decode the text from ASCII to String 
    except:
        return False

