import time
from socket import socket, AF_INET, SOCK_DGRAM


def send_img(address):
    sock = socket(AF_INET, SOCK_DGRAM)

    with open('front_in.jpg', 'rb') as f:
        dat = f.read()

    n = 10
    step = len(dat) // n + 1
    cnt = 0
    for i in range(0, len(dat), step):
        sock.sendto(dat[i:i + step], address)
        cnt += 1
        time.sleep(0.001)
        # print(len(dat[i:i + step]))
    print(len(dat), cnt)
    assert cnt == n


if __name__ == '__main__':
    send_img(('127.0.0.1', 6790))
