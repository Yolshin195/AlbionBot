import socket
import sys
import time

from Protacol import Protacol

class Server:
    def __init__(self, port, protacol, logger=print):
        self.logger = logger
        self.port = port
        self.protacol = protacol 

    #def __del__(self):
    #    self.serv_sock.close()


    def run_server(self):
        self.serv_sock = self.create_server_sock(self.port)
        cid = 0
        while True:
            client_sock = self.accept_client_conn(self.serv_sock, cid)
            self.server_client(client_sock, cid)
            cid += 1

    def create_server_sock(self, server_port):
        serv_sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  proto=0)
        serv_sock.bind(('', server_port))
        serv_sock.listen()

        self.logger(f'Server running on port {server_port}')

        return serv_sock

    def accept_client_conn(self, server_sock, cid):
        client_sock, client_addr = server_sock.accept()
        self.logger(f'Client #{cid} connect '
                    f'{client_addr[0]}:{client_addr[1]}')
        return client_sock

    def server_client(self, client_sock, cid):
        request = self.read_request(client_sock)
        if request is None:
            self.logger(f'Client #{cid} unexpectedly disconnected')
        else:
            response = self.handle_request(request)
            self.write_response(client_sock, response, cid)

    def read_request(self, client_sock):
        return self.protacol.read(client_sock)

    def handle_request(self, request):
        time.sleep(5)
        return request[::-1]

    def write_response(self, client_sock, response, cid):
        self.protacol.write(client_sock, response)
        client_sock.close()
        self.logger(f'Client #{cid} has been served')


if __name__== '__main__':
    protacol = Protacol(10)
    server = Server(4000, protacol)
    server.run_server()
