import sys
import os
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt(msg, algo):

    if algo == 'AES':
        key = os.urandom(32)
        write_txt("key", key)      # generate a file that saves the key
        algorithm = algorithms.AES(key)
        iv = os.urandom(16)
        write_txt("iv", iv)        # generate a file that saves the iv
        cipher = Cipher(algorithm, modes.CBC(iv))
        message = padd(msg)         # padding required 
    
    elif algo == 'ChaCha20':
        key = os.urandom(32)
        write_txt("key", key)      # generate a file that saves the key
        nonce = os.urandom(16)
        write_txt("nonce", nonce)  # generate a file that saves nonce 
        algorithm = algorithms.ChaCha20(key, nonce)
        cipher = Cipher(algorithm, mode=None)
        message = msg               # no padding required
        
    else:
        print("Error: Unknown algorithm")
        exit(0)

    encryptor = cipher.encryptor()
    return (encryptor.update(message) + encryptor.finalize())


def padd(msg):
    padder = padding.PKCS7(128).padder()
    padded_msg = padder.update(msg)
    padded_msg += padder.finalize()
    return padded_msg

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
        exit(1)
        
    filename = sys.argv[1]
    algo = sys.argv[2]
    
    if not os.path.exists(filename):
        print('File does not exist')
        
    print(f'\nEncrypting {filename} using {algo}\n')
    

    if filename.endswith('.bmp'):
        msg = read_file_data(filename)
    else:
        msg = read_file_data(filename)

    msg_encrypted = encrypt(msg, algo)

    
    write_bmp("encrypted", msg_encrypted)          # generate txt with encrypted text

    
    
    print(msg)
    print(msg_encrypted)


if __name__ == "__main__":
    main()