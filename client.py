import pickle
import cv2 as cv
import numpy
import socket
import mss
import time
import gzip
import sys

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1234))
s.connect((sys.argv[1], int(sys.argv[2])))

monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
with mss.mss() as sct:
    while True:
        frame = numpy.array(sct.grab(monitor))
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #ret, frame = cv.imencode('.jpg', frame)

        pack = pickle.dumps(frame)
        pack = gzip.compress(pack)
        packSize = bytes(f'{len(pack):<10}', 'utf-8')
        s.sendall(packSize + pack)

        full_msg = b''
        new_msg = True
        while True:
            msg = s.recv(1024)

            if new_msg:
                print(f'new message length: {msg[:HEADERSIZE]}')
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg

            if len(full_msg) - HEADERSIZE == msglen:
                print("full msg recvd")

                body = pickle.loads(full_msg[HEADERSIZE:])
                print(body)
                if body['action'] == 'stop': 
                    s.close()
                    exit()



