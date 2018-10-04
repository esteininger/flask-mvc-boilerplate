from Crypto.Cipher import XOR
import base64
from config import secretKey

def encrypt(plaintext):
  cipher = XOR.new(secretKey)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(ciphertext):
  cipher = XOR.new(secretKey)
  return cipher.decrypt(base64.b64decode(ciphertext))
