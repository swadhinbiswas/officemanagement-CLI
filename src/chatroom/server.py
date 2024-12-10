import socket
import threading

from rich.console import Console
from rich.text import Text

class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5080
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.nicknames = []

        # Initialize Rich console for logging
        self.console = Console()

    def start(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen()
            self.console.print(f"[bold green]Server is running and listening on {self.host}:{self.port}[/bold green]")
        except socket.error as e:
            self.console.print(f"[bold red]Error binding server socket: {e}[/bold red]")
            return

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message)
            except Exception:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(self.style.warn(f"{nickname} has left the chat.".encode("ascii")))

    def handle(self, client):
        try:
            while True:
                try:
                    message = client.recv(1024)
                    if message:
                        self.broadcast(message)
                    else:
                        break
                except Exception:
                    if client in self.clients:
                        index = self.clients.index(client)
                        self.clients.remove(client)
                        client.close()
                        nickname = self.nicknames[index]
                        self.nicknames.remove(nickname)
                        self.broadcast(self.style.warn(f"{nickname} has left the chat.".encode("ascii")))
                        break
        except Exception as e:
            self.console.print(f"[bold red]Unexpected error in handle: {e}[/bold red]")

    def receive(self):
        try:
            while True:
                client, address = self.server.accept()
                self.console.print(f"[bold cyan]Connected with {str(address)}[/bold cyan]")

                client.send("Nickname:".encode("ascii"))
                nickname = client.recv(1024).decode("ascii")
                self.nicknames.append(nickname)
                self.clients.append(client)

                self.console.print(f"[bold yellow]Nickname of the client is {nickname}[/bold yellow]")

                self.broadcast(f"{nickname} has joined the chat!".encode("ascii"))
                client.send("Connected to the server!".encode("ascii"))

                thread = threading.Thread(target=self.handle, args=(client,))
                thread.start()

                self.console.print(f"[bold green]Active connections: {threading.activeCount() - 1}[/bold green]")
        except socket.error as e:
            self.console.print(f"[bold red]Socket error occurred in receive: {e}[/bold red]")
        except Exception as e:
            self.console.print(f"[bold red]Unexpected error occurred in receive: {e}[/bold red]")


if __name__ == "__main__":
    server = Server()
    server.start()
    server.receive()
