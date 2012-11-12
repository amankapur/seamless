from socket import *

HOST = 'localhost'
PORT = 29876
ADDR = (HOST,PORT)
BUFSIZE = 4096

cli = socket(AF_INET, SOCK_STREAM)
cli.connect((ADDR))

try:
	while True:
		data = cli.recv(BUFSIZE)
		if data:
			print data
except KeyboardInterrupt:
	cli.close()

