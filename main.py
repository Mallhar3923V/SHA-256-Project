#This is the main file that imports the implementation of the SHA-256 hash from the sha256.py file 
from sha256 import sha256

def run_sha():
    print("-"*5, "SHA256 Hashing Function", "-"*5)
    m = input("Give a message to hash: ")
    print(f'The final Hash of the provided message is: {sha256(m)}')\
    
if __name__ == "__main__":
    run_sha()