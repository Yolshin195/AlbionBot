import pickle
import cv2 as cv
import numpy
import gzip

import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((socket.gethostname(), 1234))
s.bind(('0.0.0.0', 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    full_msg = b''
    new_msg = True
    msglen = 0
    while True:
        msg = clientsocket.recv(msglen or 1024)

        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            img = gzip.decompress(full_msg[HEADERSIZE:])
            img = pickle.loads(img)
            cv.imshow('img', img)

            pack = pickle.dumps({"action": "1"})
            packsize = bytes(f'{len(pack):<10}', 'utf-8')
            clientsocket.sendall(packsize + pack)

            new_msg = True
            full_msg = b''
            msglen = 0

        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            pack = pickle.dumps({"action": "stop"})
            packsize = bytes(f'{len(pack):<10}', 'utf-8')
            clientsocket.sendall(packsize + pack)
            clientsocket.close()
            break
