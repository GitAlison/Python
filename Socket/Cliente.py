import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=''
port=8999

s.connect((host,port))

dados = s.recv(1024)

print(dados.decode('utf-8'))
