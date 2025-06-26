from cryptography.fernet import Fernet

# Load the secret key from the file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

# Create Fernet object
fernet = Fernet(key)


data = "This is a test log"
encrypted_data = fernet.encrypt(data.encode())

print("Encrypted:", encrypted_data)

decrypted_data = fernet.decrypt(encrypted_data)
print("Decrypted:", decrypted_data.decode())
