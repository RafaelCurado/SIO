import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

KeyLengths = [1024, 2048, 3072, 4096]

def main():

    if len(sys.argv) < 2:
        print("Missing key length") 
        exit(0)

    key_length = int(sys.argv[1])

    if key_length not in KeyLengths:
        print("Invalid key length\nMust be 1024, 2048, 3072 or 4096") 
        exit(0)
    
    print("RSA key lenght: ", key_length)

    private_key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = key_length,
    )

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key = private_key.public_key()
    
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("private_key.pem", "wb") as f:
        f.write(private_pem)
    
    with open("public_key.pem","wb") as f:
        f.write(public_pem)

if __name__ == '__main__':
    main()