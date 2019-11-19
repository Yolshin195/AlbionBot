from Server import Server
from Protacol import Protacol

class ControlServer(Server):
    def handle_request(self, request):
        self.logger(f'handler_request begin')
        response = bytearray()



        self.logger(f'handler_request end')
        return response

if __name__== '__main__':
    protacol = Protacol(10)
    server = ControlServer(4002, protacol, print)
    server.run_server()
