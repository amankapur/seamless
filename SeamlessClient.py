#import logging

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout

import socket
import os, os.path
import time
from xml.dom.minidom import parse, parseString


class SeamlessChat(ClientXMPP):
    def __init__(self, jid, password):
        
        ClientXMPP.__init__(self, jid, password)
        self.Recv_data = 0
        self.Send_data = 0

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.recvMsg)

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

    def recvMsg(self, msg):
        print "Message received!"

        string = str(msg)
        proc = parseString(string)
        inner = proc.getElementsByTagName("body")[0].firstChild
        self.Recv_data = inner.nodeValue
        
        #server.send(self.Recv_data)
        print self.Recv_data

    def sendMsg(self, msg, sendto):
        self.send_message(mto=sendto,
                          mbody=msg,
                          mtype='chat')

    def exit(self):
        self.disconnect()
'''
if os.path.exists( "/tmp/python_unix_sockets_example" ):
        os.remove( "/tmp/python_unix_sockets_example" )
print "Opening socket..."
server = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
server.bind("/tmp/python_unix_sockets_example")

xmpp = SeamlessChat('butteryseamless@gmail.com', 'OlinCollege')
xmpp.use_signals(signals=['SIGHUP','SIGTERM','SIGINT'])
xmpp.connect()
xmpp.process(block=False)

print "Listening..."
while 1:
        datagram = server.recv( 1024 )
        if not datagram:
                break
        else:
                print "-" * 20 + " Fwd datagram to olinseamlesstest@gmail.com: "
                print datagram
                if "DONE" == datagram:
                        xmpp.disconnect()
                        break
                elif "PRINTRECV" == datagram:
                        print xmpp.Recv_data
                elif "GET" == datagram:
                        print "SeamlessClient was just told to send"
                        #conn, addr = server.accept()
                        #print "Got connection from " + str(addr)
                        #conn.send(xmpp.Recv_data)
                        print "SeamlessClient has sent"
                else:
                        xmpp.sendMsg(datagram)

print "-" * 20 + " Shutting down..."
server.close()
os.remove( "/tmp/python_unix_sockets_example" )
print "Done"
'''
