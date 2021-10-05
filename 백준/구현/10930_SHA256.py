import hashlib

def SHA_256():
     input_data =input()
     encoded_data =input_data.encode()
     result = hashlib.sha256(encoded_data).hexdigest()
     print(result)

if __name__ == "__main__":
    SHA_256()