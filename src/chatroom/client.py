import socket
import threading
import unicodedata
from rich.console import Console

class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5080
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.console = Console()  # Initialize Rich console

        try:
            self.client.connect((self.host, self.port))
            self.nickname = self.convert_to_ascii(input("Choose a nickname: "))
            self.client.send(self.nickname.encode('ascii'))
        except socket.error as e:
            self.console.print(f"[bold red]Error connecting to server: {e}[/bold red]")
            return

        # Start receive and write threads
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        write_thread = threading.Thread(target=self.write)
        write_thread.start()

    def convert_to_ascii(self, text):
        """Ensure nickname is in ASCII only."""
        return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

    def receive(self):
        """Listen for messages from the server."""
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == "Nickname:":
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    # Print received message with Rich styling
                    self.console.print(f"[bold green]{message}[/bold green]")
            except socket.error as e:
                self.console.print(f"[bold red]Socket error: {e}[/bold red]")
                self.client.close()
                break

    def write(self):
        """Send messages to the server."""
        while True:
            # Styled input prompt for the user
            message = self.console.input(f"[bold cyan]{self.nickname}:[/bold cyan] ").strip()
            if message:
                self.client.send(f"{self.nickname}: {message}".encode('ascii'))
            else:
                self.console.print("[bold yellow]Empty message, not sent![/bold yellow]")


if __name__ == "__main__":
    x=Client()
    x.receive()
    x.write()

    