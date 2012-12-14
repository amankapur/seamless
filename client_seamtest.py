import socket
import os, os.path
import SeamlessClient as chat

seamless = chat.SeamlessChat('olinseamlesstest@gmail.com', 'seamless1')
seamless.use_signals(signals=['SIGHUP','SIGTERM','SIGINT'])
seamless.connect()
seamless.process(block=False)
while 1:
        try:
                x = raw_input( "> " )
                if "" != x:
                        print "SEND:", x
                        seamless.sendMsg( x, "butteryseamless@gmail.com" )
        except KeyboardInterrupt, k:
                print "Shutting down."
                seamless.disconnect()
                break
print "Done"
