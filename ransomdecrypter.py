import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "randsom.py" or file == "generatedkey.key" or file=="ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)


with open("generatedkey.key", "rb") as  files:
    secret_key_file = files.read()

for the_files in file_list:
    with open(the_files, "rb") as files:
        content = files.read()

    contents_decrypter = Fernet(secret_key_file).decrypt(content)
    
    with open(the_files, "wb") as files:
        files.write(contents_decrypter)