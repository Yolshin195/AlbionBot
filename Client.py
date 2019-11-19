import socket

class Client:
    def __init__(self, host_name, port, protacol, logger=print):
        self.host_name = host_name
        self.port = port
        self.protacol = protacol
        self.logger = logger

    def create_socket(self):
        client_sock = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        client_sock.connect((self.host_name, self.port))
        return client_sock

    def write_request(self, request): pass
    def read_respons(self): pass


if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 4000))
    client_sock.sendall(b'Hello, world!')
    data = client_sock.recv(1024)
    client_sock.close()
    print('Received', repr(data))
