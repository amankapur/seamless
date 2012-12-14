import socket
import os, os.path
import SeamlessClient

print "Connecting..."
if os.path.exists( "/tmp/python_unix_sockets_example" ):
        client = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
        client.connect( "/tmp/python_unix_sockets_example" )
        print "Ready."
        print "Ctrl-C to quit."
        print "Sending 'DONE' shuts down the server and quits."
        while 1:
                try:
                        x = raw_input( "> " )
                        if "" != x:
                                print "SEND:", x
                                client.send( x )
                                if "DONE" == x:
                                        print "Shutting down."
                                        break
                                elif "GET" == x:
                                        print "Getting from SeamlessClient"
                                        recvmsg = client.recv( 1024 );
                                        print "Got it!"
                                        print recvmsg
                except KeyboardInterrupt, k:
                        print "Shutting down."
                        client.close()
else:
        print "Couldn't Connect!"
        print "Done"
