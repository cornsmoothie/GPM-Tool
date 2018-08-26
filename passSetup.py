#This is for users to easily generate their own pass and key file. 
#This creates an ecrypted password and the corresponding key which are stored locally on the machine.
#This unofficial API uses cleartext passwords so we don't just want to have passwords laying around.

from cryptography.fernet import Fernet
import getpass
import os.path


def setAuth():

    passPath = ("./Auth/pw")
    keyPath = ("./Auth/key")

    file_handle(passPath)
    file_handle(keyPath)

    password = getpass.getpass('Password:')

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encryptedPassBytes = cipher_suite.encrypt(b'{password}')

    passFile = open(passPath , "wb")
    keyFile = open(keyPath , "wb")

    passFile.write(encryptedPassBytes)
    keyFile.write(key)

def file_handle(filename):
    print(filename)
    if not os.path.exists(filename):
        try:
            # os.makedirs(os.path.dirname(filename))
            print("You're good")
        except OSError as exc: # Guard against race condition
            # if exc.errno != errno.EEXIST:
                raise
    else:
        print(f"File {filename} already exists, either use this file or delete it")
        exit()

if __name__ == "__main__":
    setAuth()
    
# if passPath.isfile():
#     print("Password File already exists")
#     flag = True
# if keyPath.isfile():
#     print("Password File already exists")
#     flag = True

# if flag == True:
#     exit()
