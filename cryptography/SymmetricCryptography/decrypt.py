import sys
import os
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decrypt(msg, algo):
   
    if algo == 'AES':                           # assuming CBC mode
        key = read_file_data("key.txt")
        algorithm = algorithms.AES(key)
        iv = read_file_data("iv.txt")
        cipher = Cipher(algorithm, modes.CBC(iv))
    
    elif algo == 'ChaCha20':            
        key = read_file_data("key.txt")
        nonce = os.urandom(16)
        nonce = read_file_data("nonce.txt")
        algorithm = algorithms.ChaCha20(key, nonce)
        cipher = Cipher(algorithm, mode=None)
        
    else:
        print("Error: Unknown algorithm")
        exit(0)

    decryptor = cipher.decryptor()
    msg_decrypted = decryptor.update(msg) + decryptor.finalize()
    
    if algo == 'AES':
        return unpad(msg_decrypted)
    return msg_decrypted

def unpad(msg):
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(msg)
    message += unpadder.finalize()
    return message


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
    
    print(f'\nDecrypting {filename} using {algo}\n')
    
    if not os.path.exists(filename):
        print('File does not exist')
        
    msg_encrypted = read_file_data(filename)
    msg_decrypted = decrypt(msg_encrypted, algo)
    write_bmp("decrypted", msg_decrypted)          # generate txt with decrypted text

    print(msg_encrypted)
    print(msg_decrypted)


    
if __name__ == "__main__":
    main()