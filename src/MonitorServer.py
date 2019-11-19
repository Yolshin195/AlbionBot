import cv2 as cv
import numpy
import mss

from lib.Server import Server
from lib.Protacol import Protacol

monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
class MonitorServer(Server):
    def handle_request(self, request):
        with mss.mss() as sct:
            frame = numpy.array(sct.grab(monitor))
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            return frame;

if __name__== '__main__':
    protacol = Protacol(10)
    server = MonitorServer(4001, protacol, print)
    server.run_server()
