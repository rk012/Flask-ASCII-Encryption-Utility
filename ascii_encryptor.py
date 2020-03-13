import random

def encrypt(seed, message):
  random.seed(seed)
  encryptedmessage=""
  for i in range(0, len(message)):
    encryptedchar = chr((((ord(message[i])-32)+random.randint(0, 94))%95)+32)
    if encryptedchar == '#':
      encryptedmessage=encryptedmessage+'%23'
    elif encryptedchar == '%':
      encryptedmessage=encryptedmessage+'%25'
    elif encryptedchar == '&':
      encryptedmessage=encryptedmessage+'%26'
    else:
      encryptedmessage=encryptedmessage+encryptedchar

  return "--"+encryptedmessage+"--"

def decrypt(seed, encryptedmessage):
  random.seed(seed)
  message=""

  for i in range(2, len(encryptedmessage)-2):
    message = message+chr((((ord(encryptedmessage[i])-32)-random.randint(0, 94))%95)+32)

  return message
