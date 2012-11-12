from socket import * 

HOST = ''
PORT = 29876
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket(AF_INET, SOCK_STREAM)

serv.bind((ADDR))
serv.listen(5)

print 'listening...'

conn,addr = serv.accept()
try:
	print 'data sent'
	conn.send('TEST')
except KeyboardInterrupt:
	conn.close()	


