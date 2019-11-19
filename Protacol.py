import pickle
import gzip

class Protacol:
    def __init__(self, header_size, logger=print):
        self.header_size = header_size
        self.logger = logger

    def write(self, sock, response):
        response = pickle.dumps(response)
        response = gzip.compress(response)

        response_size = bytes(
            f'{len(response):<{self.header_size}}', 'utf-8')
        sock.sendall(response_size + response)

    def read(self, sock):
        response = bytearray()
        try:
            response_size = sock.recv(self.header_size)
            if not response_size:
                #Сервер прежде временно отключился
                return None
            else:
                response_size = int(response_size)
            while True:
                chunk = sock.recv(response_size)
                if not chunk: 
                    #Сервер прежде временно отключился
                    return None
                response += chunk
                if len(response) == response_size:
                    response = gzip.decompress(response)
                    response = pickle.loads(response)
                    return response 
        except ConnectionResetError:
            #Соединение было неожиданно разорвано
            return None
        except:
            raise

