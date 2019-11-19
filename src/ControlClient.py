from lib.Client import Client

class ControlClient(Client):
    def getSizeMonitor(self):
        response = self.request({'action': 'getsize'},1)

        return response 

    def moveTo(self, x, y, s):
        response = self.request({'action': 'moveto',
            'x': x, 'y': y, 'time': s }, 2)

        return response 


if __name__ == '__main__':
    from lib.Protacol import Protacol

    protacol = Protacol(10, lambda log: None)
    controlClient = ControlClient('localhost', 4002, protacol)

    sizeMonitor = controlClient.getSizeMonitor()
    print(sizeMonitor)

    arrayMoveTo = controlClient.request([
        {'action': 'moveto', 'x': 100, 'y': 100, 'time': 1 },
        {'action': 'moveto', 'x': 300, 'y': 100, 'time': 1 },
        {'action': 'moveto', 'x': 300, 'y': 300, 'time': 1 },
        {'action': 'moveto', 'x': 100, 'y': 300, 'time': 1 }
        ])
    print(arrayMoveTo)

    moveTo = controlClient.moveTo(100, 100, 1)
    print(moveTo) 

