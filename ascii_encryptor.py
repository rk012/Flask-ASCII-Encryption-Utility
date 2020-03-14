import random

def encrypt(seed, message):
  random.seed(seed)
  encryptedmessage=""
  for i in range(0, len(message)):
    encryptedmessage=encryptedmessage+chr((((ord(message[i])-32)+random.randint(0, 94))%95)+32)

  return "--"+encryptedmessage+"--"

def decrypt(seed, encryptedmessage):
  random.seed(seed)
  message=""

  for i in range(2, len(encryptedmessage)-2):
    message = message+chr((((ord(encryptedmessage[i])-32)-random.randint(0, 94))%95)+32)

  return message
