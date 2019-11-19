import cv2 as cv
import numpy

import socket
import time

from Protacol import Protacol


if __name__ == '__main__':
    protacol = Protacol(10)

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 4000))
    protacol.write(client_sock, '<get><img></img></get>')
    data = protacol.read(client_sock)
    client_sock.close()

    cv.imshow('Monitor clietn', data)
    cv.waitKey(0)
    print('Received', repr(data))
