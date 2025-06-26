# Keylogger with Encrypted Data Exfiltration
Introduction
This project demonstrates an educational Proof of Concept (PoC) for a keylogger that securely
captures, encrypts, and logs keystrokes on a local system. It also simulates data exfiltration to a
localhost HTTP server, with a built-in kill switch for safe termination.
Abstract
The goal of this project is to build a keylogger with encrypted log storage using the Fernet symmetric
encryption method. The project captures keystrokes in real time, encrypts each log, writes it to a file,
and simulates sending the encrypted data to a localhost HTTP server. A decryption utility and a kill
switch are included to manage and control execution ethically.
Tools Used
- Python 3.13
- pynput (keyboard capturing)
- cryptography (Fernet encryption)
- requests (HTTP data simulation)
- PyInstaller (optional for .exe packaging)
Steps Involved in Building the Project
1. Generate a symmetric encryption key using Fernet.
2. Develop a keylogger using pynput to capture keystrokes.
3. Encrypt each captured keystroke and log it to a binary file.
4. Simulate data exfiltration by POSTing encrypted data to a localhost HTTP server.
5. Implement a kill switch to stop keylogger execution safely.
6. Create a log decryption utility to read and decrypt saved logs.
