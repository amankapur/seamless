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
