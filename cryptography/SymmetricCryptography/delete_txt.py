import os


files = [f for f in os.listdir('.') if os.path.isfile(f) and "filename" not in f]

for f in files:
    if f.endswith('.txt'):
        print('Deleting file: ', f)
        os.remove(f)
