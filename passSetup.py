#This is for users to easily generate their own pass and key file. 
#This creates an ecrypted password and the corresponding key which are stored locally on the machine.
#This unofficial API uses cleartext passwords so we don't just want to have passwords laying around.

from cryptography.fernet import Fernet
import getpass
import os.path

if __name__ == "__main__":
    setAuth()

def setAuth():
    password = getpass.getpass('Password:')

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encryptedPassBytes = cipher_suite.encrypt(b'{password}')

    passPath = Path("./Auth/pw")
    keyPath = Path("./Auth/key")

    file_handle(passPath)
    file_handle(keyPath)

    passFile = open("passPath" , "w")
    keyFile = open("keyPath" , "w")

    passFile.write(encryptedPassBytes)
    keyFile.write(key)

def file_handle(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    else:
        print("File {filename} already exists, either use this file or delete it")
        exit()

    
# if passPath.isfile():
#     print("Password File already exists")
#     flag = True
# if keyPath.isfile():
#     print("Password File already exists")
#     flag = True

# if flag == True:
#     exit()
