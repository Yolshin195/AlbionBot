import time

from Protacol import Protacol


if __name__ == '__main__':
    protacol = Protacol(10)

    while True:
        start = time.time()

        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('127.0.0.1', 4002))

        protacol.write(client_sock, '<get><img></img></get>')
        data = protacol.read(client_sock)
        client_sock.close()
        print(f'Get img time: {time.time() - start}')

        cv.imshow('Monitor clietn', data)
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
