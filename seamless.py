import sublime, sublime_plugin

# create an asynchronous communication stream (messaging protocol)
# have to send the 'view' object on modified to clients
# use the picklejson library to serialize the 'view' object on both ends


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		""" 

		TO DO :

		sublime EVENT LISTEn on_modified(view)	
			seialize view into json
			send to client
			
		
		seamless event listener on_receive(data)
			unserialize(data) from json to view
			update current view with data
