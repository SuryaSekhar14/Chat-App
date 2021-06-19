import rsa
import encrypt
import decrypt

message = input()
pub_key,prvt_key = rsa.newkeys(512)
res = encrypt.encryptmsg(message,pub_key)
unres = decrypt.decryptmsg(res,prvt_key)

print("Encrypted Message: ",res)
print("Decrypted Message: ",unres)