import socket
import os, os.path
import SeamlessClient as chat

seamless = chat.SeamlessChat('butteryseamless@gmail.com', 'OlinCollege')
seamless.use_signals(signals=['SIGHUP','SIGTERM','SIGINT'])
seamless.connect()
seamless.process(block=False)
while 1:
        try:
                x = raw_input( "> " )
                if "" != x:
                        print "SEND:", x
                        seamless.sendMsg( x,"olinseamlesstest@gmail.com" )
        except KeyboardInterrupt, k:
                print "Shutting down."
                seamless.disconnect()
                break
print "Done"
