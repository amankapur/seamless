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

    def recvMessage(self, msg):
        self.Recv_data = msg;
        print "******************************************" + self.Recv_data

    def sendMessage(self, msg):
        self.send_message(mto="james.wu.jimmy@gmail.com",
                          mbody=msg,
                          mtype='chat')

    def SeamlessStart():
        #logging.basicConfig(level=logging.DEBUG,
        #                    format='%(levelname)-8s %(message)s')

        xmpp = SeamlessChat('butteryseamless@gmail.com', 'OlinCollege')
        xmpp.use_signals(signals=['SIGHUP','SIGTERM','SIGINT'])
        xmpp.connect()
        xmpp.process(block=False)

    def exit():
        xmpp.disconnect()
