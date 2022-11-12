import sys
import os   
from cryptography.hazmat.primitives import hashes

def hash_selector(hash):
    if hash == "SHA":
        return hashes.SHA256()
    if hash == "BLAKE2":
        return hashes.BLAKE2b(64)
    if hash == "MD5":
        return hashes.MD5()
    else:
        print("Unknown hash")
        exit(0)

def hash_data(data, hash):
    algo = hash_selector(hash)
    digest = hashes.Hash(algo)
    digest.update(data)
    return digest.finalize()

def flip_data(data):
    adata = bytearray(data)
    return None
    

    
def write_data(filename, msg):
    file = open(f"{filename}.txt","wb")
    file.write(msg)
    return None

def read_file_data(filename):
    data = None
    with open(filename, 'rb') as file:
        data = file.read()
    return data

def main():
    input = sys.argv[1]
    hash = sys.argv[2]

    if(len(sys.argv) < 3):
        print("\nMissing args")
        exit(0)

    if not os.path.exists(input):
        print('\nFile does not exist')
        exit(0)

    print(f"\nHashing {input} using {hash}")

    data = read_file_data(input)
    data_hash = hash_data(data, hash)
    data_hash_flipped = flip_data(data_hash)

    print(data_hash)
    #write_data("hashes",data_hash)
    #write_data("hashes_flipped",data_hash_flipped)

if __name__ == '__main__':
    main()