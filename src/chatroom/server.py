import socket
import threading
from src.design.stylr import Style

class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5080
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.nicknames = []
        self.style=Style()

    def start(self):

        try:
            self.server.bind((self.host, self.port))
            self.server.listen()
            print(f"Server is running and listening on {self.host}:{self.port}")
        except socket.error as e:
            print(f"Error binding server socket: {e}")
            return

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f"{nickname} has left the chat.".encode("ascii"))

    def handle(self, client):
        try:
            while True:
                try:
                    message = client.recv(1024)
                    self.broadcast(message)
                except:
                    if client in self.clients:
                        index = self.clients.index(client)
                        self.clients.remove(client)
                        client.close()
                        nickname = self.nicknames[index]
                        self.nicknames.remove(nickname)
                        self.broadcast(f"{nickname} has left the chat.".encode("ascii"))
                        break
        except Exception as e:
            print(f"Unexpected error in handle: {e}")

    def receive(self):
        try:
            while True:
                client, address = self.server.accept()
                print(f"Connected with {str(address)}")

                client.send("NICK".encode("ascii"))
                nickname = client.recv(1024).decode("ascii")
                self.nicknames.append(nickname)
                self.clients.append(client)

                print(f"Nickname of the client is {nickname}")
                self.broadcast(f"{nickname} has joined the chat!".encode("ascii"))
                client.send("Connected to the server!".encode("ascii"))

                thread = threading.Thread(target=self.handle, args=(client,))
                thread.start()

                print(f"Active connections {threading.activeCount() - 1}")
        except socket.error as e:
            print(f"Socket error occurred in receive: {e}")
        except Exception as e:
            print(f"Unexpected error occurred in receive: {e}")
