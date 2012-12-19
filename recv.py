import socket
import os, os.path
import time
import sys

#import SeamlessClient as chat
import SeamlessClient as chat


seamless = chat.SeamlessChat('olinseamlesstest@gmail.com', 'seamless1')
seamless.use_signals(signals=['SIGHUP','SIGTERM','SIGINT'])
seamless.connect()
seamless.process(block=False)


os_path = "/tmp/seamless-send"



if os.path.exists( os_path):
        os.remove( os_path )
print "Opening socket..."
server2 = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
server2.bind(os_path)
             
print "Listening..."
while True:
        datagram = server2.recv( 1024 )
        if datagram:
                #print "-" * 20
                print datagram
                seamless.sendMsg(datagram,"butteryseamless@gmail.com" )
                print "datagram sent"
                # chat.send(datagram)

print "-" * 20
print "Shutting down..."
server2.close()
os.remove( os_path )
print "Done"

