import subprocess
import os
import platform

# Get the base directory of the current script
base_directory = os.path.dirname(os.path.abspath(__file__))
serverpath = os.path.join(base_directory, "server.py")
clientpath = os.path.join(base_directory, "client.py")

class Chatroom:
    def __init__(self):
        self.platform = platform.system()

    def create_chatroom(self):
        if os.name=="posix":
            subprocess.Popen(['gnome-terminal', '--', 'python', serverpath])
           
    def join_chatroom(self):
        if os.name=="posix":
            subprocess.Popen(['gnome-terminal', '--', 'python', clientpath])
        


