import socket
import sys
import time

class Client:
    def __init__(self, host_name='localhost', port=4000, logger=print):
        self.client_sock = self.create_client_sock()
        self.host_name   = host_name
        self.port        = port
        self.logger      = print

    def __del__(self):
        self.client_sock.close()

    def create_client_sock(self):
        client_sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  proto=0)
        return client_cock 

    def write_request(self, client_sock, request):
        client_sock.sendall(request)

    def read_response(self, client_sock, delimiter):
        response = bytearray()
        try:
            while True:
                chunk = client_sock.recv(4)
                if not chunk: 
                    #Сервер прежде временно отключился
                    return None
                response += chunk
                if delimiter in response:
                    return response 
        except ConnectionResetError:
            #Соединение было неожиданно разорвано
            return None
        except:
            raise

    def handle_request(self, request, delimiter='H'):
        self.client_sock.connect((self.host_name, self.port))
        self.client_sock.write_request(self.client_sock, request)
        response = self.read_response(self.client_sock, delimiter)
        if response is None:
            self.logger(f'Server {self.host_name}:{self.port} '
                        f'unexpectedly disconnected')
            return response
            self.client_sock.close()
        else:
            return response
            self.client_sock.close()


if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 4000))
    client_sock.sendall(b'Hello, world!')
    data = client_sock.recv(1024)
    client_sock.close()
    print('Received', repr(data))
