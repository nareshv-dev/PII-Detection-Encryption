import random
import string 

chars=""+ string.punctuation+ string.digits+ string.ascii_letters
chars= list(chars)
keys= chars.copy()

random.shuffle(keys)

#Encrpyt
plain_text= input("Enter the encrypt message:")
cipher_text =""

for letter in plain_text:
    index= chars.index(letter)
    cipher_text += keys[index]


print("Encrpyted message:",cipher_text)

#Decrpyt
cipher_text= input("Enter the encrypt message:")
plain_text =""

for letter in cipher_text:
    index= keys.index(letter)
    plain_text += chars[index]


print("Original message:",plain_text)


