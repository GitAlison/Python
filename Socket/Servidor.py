import socket 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=''
port=8999

s.bind((host,port))
s.listen(1)
msg= 'Olá Cliente'

while True:
	c,e = s.accept()
	print('conectado com',e)
	c.send(msg.encode('utf-8'))
	c.close()
