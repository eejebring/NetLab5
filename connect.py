import socket


class GameCom:

    def __init__(self, port = 60003):
        self.connection = None
        self._port = port
        self._socket = socket.socket()

    def open_server(self):
        self._socket.bind(("", self._port))
        print(f"port opened on {self._port}")
        self._socket.listen(5)
        while True:
            self.connection, addr = self._socket.accept()
            print('Got connection from', addr)
            break

    def connect_to_server(self, ip="127.0.0.1"):
        self._socket.connect((ip, self._port))
        self.connection = self._socket

    def wait_for_response(self):
        while True:
            response = self.connection.recv(1024).decode()
            if response != "":
                return response

    def send(self, msg):
        self.connection.send(msg.encode())

    def close(self):
        self._socket.close()
