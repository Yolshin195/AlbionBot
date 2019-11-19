import cv2 as cv
import numpy
import mss

from Server import Server;
from Protacol import Protacol

monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
class MonitorServer(Server):
    def handle_request(self, request):
        self.logger(f'handler_request begin')
        with mss.mss() as sct:
            frame = numpy.array(sct.grab(monitor))
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            self.logger(f'handler_request end')
            return frame;

if __name__== '__main__':
    protacol = Protacol(10)
    server = MonitorServer(4000, protacol, print)
    server.run_server()
