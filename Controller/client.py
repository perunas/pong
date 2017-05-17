import socket

ip = input('Input IP: ')
#ip = '84.237.53.77'
#ip = '255.255.255.255'
#port = int(input('Input port: '))
port = 9090

server_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while 1:
    message = bytes(input("Enter text: "), 'utf-8')
    if 'exit' in message.decode('utf-8'):
        break
    server_connection.sendto(message, (ip, port))
