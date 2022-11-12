import sys
import os
from cryptography import x509
from datetime import datetime

def valid_cert(cert):
    now = datetime.now()
    return (cert.not_valid_after > now) and (cert.not_valid_before < now)

def read_file_data(filename):
    data = None
    with open(filename, 'rb') as file:
        data = file.read()
    return data

# def load_certs_with_regex(data):
#     s_delim = '-----BEGIN CERTIFICATE-----'
#     e_delim = '-----BEGIN CERTIFICATE-----'
#     regex = f'(' + s_delim + '.*?' + e_delim + ')'
#     return re.

def main():

    if len(sys.argv) < 2:
        print("missing certificate file")
        exit(0)
    filename = sys.argv[1]  

    if not os.path.exists(filename):
        print('File does not exist')
        exit(0)
    print(f"Validating {filename} certificate\n")

    pem_data = read_file_data(filename)
    print(pem_data)
    print('\n')

    cert = x509.load_pem_x509_certificate(pem_data)
    print(cert)

    print(datetime.now())
    print(valid_cert(cert))


if __name__ == '__main__':
    main()

