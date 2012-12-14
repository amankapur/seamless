import socket
import os, os.path
import SeamlessClient as chat

seamless = chat.SeamlessChat('butteryseamless@gmail.com', 'OlinCollege')
seamless.use_signals(signals=['SIGHUP','SIGTERM','SIGINT'])
seamless.connect()
seamless.process(block=False)


print "Connecting..."
os_path = "/tmp/seamless-recv"


if os.path.exists( os_path ):
        ipc = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
        ipc.connect(os_path)
        print "Ready."
        print "Ctrl-C to quit."
        print "Sending 'DONE' shuts down the server and quits."

        
        old_x = ""
        while True:
                try:
                        x = str(seamless.Recv_data)
                        if x != old_x:
                               if "" != x:
                                       print "SEND:", x
                                       ipc.send( x )
                                       old_x = x
        
                except KeyboardInterrupt, k:
                        print "Shutting down."
                        ipc.close()
else:
        print "Couldn't Connect!"
        print "Done"
