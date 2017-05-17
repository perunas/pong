import socket

ip = input('Input IP: ')
port = input('Input port: ')

sock = socket.socket()
sock.connect((ip, port))

text = bytes(input('Write text: '), 'utf-8')
sock.send(text)

data = sock.recv(1024)
sock.close()

print(data)
