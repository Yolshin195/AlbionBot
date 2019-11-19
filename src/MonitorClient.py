from lib.Client import Client
import time

class MonitorClient(Client):
    def getImg(self):
        img = self.request('<getimg/>')

        return img


if __name__ == '__main__':
    from lib.Protacol import Protacol
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

