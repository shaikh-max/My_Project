import os, sys

def check_kill_switch():
    if os.path.exists("kill.switch"):
        print("Kill switch activated. Exiting...")
        sys.exit()
