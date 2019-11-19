# python3

import pickle
import cv2 as cv
import numpy
import gzip

import sys
import time
from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer

HEADERSIZE = 10
class MyTCPHandler(BaseRequestHandler):
  def handle(self):
    full_msg = b''
    new_msg = True
    msglen = 0
    while True:
        msg = self.request.recv(msglen or 1024)

        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            img = gzip.decompress(full_msg[HEADERSIZE:])
            img = pickle.loads(img)
            print('BEGIN img show')
            cv.imshow('img', img)
            cv.waitKey(0)
            cv.destroyAllWindows()

            pack = pickle.dumps({"action": "stop"})
            packsize = bytes(f'{len(pack):<10}', 'utf-8')
            self.request.sendall(packsize + pack)

            new_msg = True
            full_msg = b''
            msglen = 0
            print("END")
            break


class ThreadedTCPServer(ThreadingMixIn, TCPServer): pass


if __name__ == '__main__':
  host = 'localhost'
  port = int(sys.argv[1])

  with ThreadedTCPServer((host, port), MyTCPHandler) as srv:
    srv.serve_forever()
    cv.destroyAllWindows()
