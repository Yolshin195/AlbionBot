import socket
import time

class Client:
    def __init__(self, host_name, port, protacol, logger=print):
        self.address = (host_name, port)
        self.protacol = protacol
        self.logger = logger

    def create_socket(self):
        client_sock = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        return client_sock

    def request(self, body, cid=0):
        start = time.time()

        client_sock = self.create_socket()
        client_sock.connect(self.address)

        self.protacol.write(client_sock, body, cid)
        respons = self.protacol.read(client_sock, cid)

        client_sock.close()

        self.logger(f'Requvest time: {time.time() - start}')
        return respons

if __name__ == '__main__':
    from Protacol import Protacol

    protacol = Protacol(10)
    client = Client('localhost', 4001, protacol)
    data = client.request('<getimg/>', 0)

    print('Received', repr(data))

