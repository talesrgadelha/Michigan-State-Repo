import socket

meuConector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meuConector.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
meuConector.send(cmd)

while True:
    data = meuConector.recv(512)
    if len(data) < 1:
        break
    print(data.decode('utf-8'))

meuConector.close()