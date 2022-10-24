import sys
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization


def encrypt(msg, algo):

    if algo == 'RSA':
        private_key = read_pem('private_key.pem')
        #print(private_key)
        signature = private_key.sign(
            msg,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        public_key = private_key.public_key()
        public_key.verify(
            signature,
            msg,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        ciphertext = public_key.encrypt(
            msg,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return ciphertext

    else:
        print("Unknow algo")
        exit(0)

def read_pem(filename):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
    )
    return private_key


def read_file_data(filename):
    data = None
    with open(filename, 'rb') as file:
        data = file.read()
    return data
    
def write_txt(filename, msg):
    file = open(f"{filename}.txt","wb")
    file.write(msg)
    return None

def write_bmp(filename, msg):
    file = open(f"{filename}.bmp","wb")
    file.write(msg)
    return None

def main():

    if len(sys.argv) < 3:
        print("Missing args")
        exit(1)
        
    filename = sys.argv[1]
    algo = sys.argv[2]
    
    if not os.path.exists(filename):
        print('File does not exist')
        
    print(f'\nEncrypting {filename} using {algo}\n')
    
    msg = read_file_data(filename)

    msg_encrypted = encrypt(msg, algo)

    #write_txt("encrypted", msg_encrypted)          # generate txt with encrypted text

    
    #print(msg)
    print(msg_encrypted)


if __name__ == '__main__':
    main()