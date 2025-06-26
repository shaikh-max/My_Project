from cryptography.fernet import Fernet

# Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Read and decrypt logs
def decrypt_logs():
    try:
        with open("keylog.enc", "rb") as log_file:
            lines = log_file.readlines()
            print("\nDecrypted Key Logs:")
            for line in lines:
                decrypted_data = fernet.decrypt(line.strip())
                print(decrypted_data.decode())
    except FileNotFoundError:
        print("No encrypted log file found.")
    except Exception as e:
        print("Error while decrypting:", e)

decrypt_logs()

with open("keylog.enc", "rb") as log_file:
    lines = log_file.readlines()
    print("\nDecrypted Key Logs:")
    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        try:
            decrypted_data = fernet.decrypt(line)
            print(decrypted_data.decode())
        except Exception as e:
            print("Error decrypting a line:", e)
