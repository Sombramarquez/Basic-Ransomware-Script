"""

Simple script to simulate the procedure of a Ransomware attack
The script encrypts and decrypts target files'

"""""
_author_ = "Victor Marquez"
_version_ =0.2

import os
from pathlib import Path
from Crypto.Cipher import AES

#Allows script to know what files to target
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


    #Save data into a new file
    fileName = file.name.removesuffix(file.suffix)
    fileExtension = ".decrypted"
    encFile = "C:/Users/victo/Desktop/test_Folder/"+fileName + fileExtension
    with open(encFile, 'wb') as f:
        f.write(text)
        f.close()
        os.remove(file)

        
        
        
path = "Path where encrypted files are located"
for file in detectFiles(path):
    filePath = Path(file)
    fileType = filePath.suffix.lower()
    if fileType in ['.hacked!']:
        decryptFile(filePath,b'Sixyeen byte key') #Key, script will not work if keys are not the same
