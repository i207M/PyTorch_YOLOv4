from socket import socket, AF_INET, SOCK_DGRAM


def send_img(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    FILE_NAME = b'temp_input.jpg'
    sock.sendto(FILE_NAME, address)
    print(f'Sent {str(FILE_NAME, encoding = "utf-8")}')


if __name__ == '__main__':
    send_img(('127.0.0.1', 9876))
