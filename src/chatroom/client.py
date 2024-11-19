import socket
import threading
import unicodedata

class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5080
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client.connect((self.host, self.port))
            self.nickname = self.convert_to_ascii(input("Choose a nickname: "))
            self.client.send(self.nickname.encode('ascii'))
        except socket.error as e:
            print(f"Error connecting to server: {e}")
            return

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        write_thread = threading.Thread(target=self.write)
        write_thread.start()

    def convert_to_ascii(self, text):
        return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == "NICK":
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f"{self.nickname}: {input('')}"
            self.client.send(message.encode('ascii'))

