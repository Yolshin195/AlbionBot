import time
import socket
from lib.Protacol import Protacol
import cv2 as cv
import numpy

if __name__ == '__main__':
    protacol = Protacol(10)

    while True:
        start = time.time()

        client_sock = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        client_sock.connect(('localhost', 4001))

        protacol.write(client_sock, '<getimg/>')
        img =  protacol.read(client_sock)

        client_sock.close()

        print(f'get img time: {time.time() - start}')

        cv.imshow('Monitor clietn', img)
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

