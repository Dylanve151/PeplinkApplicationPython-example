import socket
from os import path
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect ( ('192.168.50.10', 2222) )

try:
	sock.sendall(('connected...\n').encode())
	print('connected...')
	while path.isfile('run.txt'):
		print('send: hi!')
		sock.sendall(('hi!\n').encode())
		sleep(1)
finally:
	print('Disconnected...')
	sock.sendall(('Disconnected... \n').encode())
	sock.close()
