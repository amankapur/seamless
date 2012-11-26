import sublime, sublime_plugin
import gnosis.xml.pickle as xml_pickle

# create an asynchronous communication stream (messaging protocol) http://coder.cl/products/pyxser/
# http://xmpppy.sourceforge.net/ 
# have to send the 'view' object on modified to clients
# use the pyxser library to serialize the 'view' object on both ends
# http://coder.cl/products/pyxser/

Send_data = 0
Recv_data = 0

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		def on_modified(self, view):
			Send_data =  xml_pickle.dumps(view)
			print Send_data
			print view

			
		" 
		TO DO :

		sublime EVENT LISTEn on_modified(view)	
			seialize view into xml
			send to client
			
		
		seamless event listener on_receive(data)
			unserialize(data) from xml to view
			update current view with data

            two global variables: sent_data and received_data
            server writes to received_data and reads send_data
            sublime writes to send_data and reads recevied_dataS
           """
class Server():
    def run(self, text):
        """
        requirements:
        (i'm reading from a constantly updated global variables)
        user A: i will have a listener which listens for changes in a global variable (send_data)
        upon an event, the listener will create an XML stream which is sent over a protocol to the IP
        server: will have a listener which listens for XML stream activity (from user B)
        when it receives an XML event, it will update user A's read_data with the information in the tag


        possible methods of sending data
        1. xmpp

        2. amqp
        http://www.rabbitmq.com/devtools.html#python-dev
        http://barryp.org/software/py-amqplib/
        http://ask.github.com/carrot/introduction.html

        later
        finding clients not hardwired through IP


        later later
        xmpp over github


        """ 
