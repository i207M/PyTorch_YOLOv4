from socket import socket, AF_INET, SOCK_DGRAM


def send_img(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    FILE_NAME = 'temp_input.jpg'
    sock.sendto(bytes(FILE_NAME, encoding='utf8'), address)
    print(f'Sent {FILE_NAME} to {address}')


if __name__ == '__main__':
    send_img(('127.0.0.1', 9876))
