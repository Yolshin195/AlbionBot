from Protacol import Protacol
from Client import Client
import time

class MonitorClient(Client):
    def getImg(self):
        start = time.time()

        client_sock = self.create_socket()

        self.protacol.write(client_sock, '<getimg/>')
        img = self.protacol.read(client_sock)

        client_sock.close()

        self.logger(f'Get img time: {time.time() - start}')
        return img


if __name__ == '__main__':
    import cv2 as cv
    import numpy


    protacol = Protacol(10)
    monitorClient = MonitorClient('localhost', 4001, protacol)

    while True:
        data = monitorClient.getImg()

        cv.imshow('Monitor clietn', data)
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

