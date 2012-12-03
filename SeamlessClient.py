import logging

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout


class SeamlessChat(ClientXMPP):
    def __init__(self, jid, password):
        
        ClientXMPP.__init__(self, jid, password)
        self.Recv_data = 0
        self.Send_data = 0
        

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.recvMessage)

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

    def recv(self, msg):
        self.Recv_data = msg;
        #print "******************************************" + self.Recv_data

    def send(self, msg):
        self.send_message(mto="amankapur91@gmail.com",
                          mbody=msg,
                          mtype='chat')

    def exit():
        xmpp.disconnect()
