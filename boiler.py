import logging

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout


class SeamlessChat(ClientXMPP):
    def __init__(self, jid, password):
        
        ClientXMPP.__init__(self, jid, password)
        self.Recv_data = 0
        self.Send_data = 0

        #self.add_event_handler("session_start", self.session_start)
        #self.add_event_handler("message", self.Recv_data)

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

    def recvMessage(self, msg):
        self.Recv_data = msg;

    def sendMessage(self, msg):
        self.send_message(mto="butteryseamless@gmail.com",
                          mbody=self.msg,
                          mtype='chat')



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    xmpp = SeamlessChat('butteryseamless@gmail.com', 'OlinCollege')
    xmpp.connect()
    xmpp.process(block=True)

    inpu = raw_input("Enter message: ")
    self.sendMessage(inpu)
