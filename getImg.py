import cv2 as cv
import socket
import sys
import cv2
import numpy
import pickle
import struct ### new code
import time
import mss
import gzip


def getImg(monitor):
    while True:
        with mss.mss() as sct:
            frame = numpy.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            yield frame

#        data = pickle.dumps(frame)
#        zdata = gzip.compress(data)
#
#        size = struct.pack("!L", len(zdata))
#        pack = size + zdata



monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
for img in getImg(monitor):
    cv2.imshow('get img: ', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
