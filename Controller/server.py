import socket

ip = input('Input IP: ')
#ip = '0.0.0.0'
#ip = '192.168.0.64'
#port = int(input('Input port: '))
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.bind((ip, port))

while 1:
    server.setblocking(False)
    try:
        message = server.recv(128)
        print(message.decode('utf-8'))
    except:
        continue
