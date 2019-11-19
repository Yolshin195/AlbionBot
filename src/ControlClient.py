from lib.Client import Client
import time

class ControlClient(Client):
    def getSizeMonitor(self):
        start = time.time()

        response = self.request({'action': 'getsize'})

        self.logger(f'Get img time: {time.time() - start}')
        return response 

    def moveTo(self, x, y, s):
        start = time.time()

        response = self.request({'action': 'moveto',
            'x': x, 'y': y, 'time': s })

        self.logger(f'Get img time: {time.time() - start}')
        return response 


if __name__ == '__main__':
    from lib.Protacol import Protacol

    protacol = Protacol(10)
    controlClient = ControlClient('localhost', 4002, protacol)

    sizeMonitor = controlClient.getSizeMonitor()
    print(sizeMonitor) 

    moveTo = controlClient.moveTo(100, 100, 10)
    print(moveTo) 

