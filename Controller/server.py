import socket

ip = input('Input IP: ')
port = int(input('Input port: '))

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(2)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    data = data.encode('utf-8')
    if 'stop' in data:
        break
    conn.send(data)

conn.close()
