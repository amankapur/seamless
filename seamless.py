import sublime, sublime_plugin
import pickle as xml_pickle
import json
import inspect
import thread
from time import sleep

# create an asynchronous communication stream (messaging protocol) http://coder.cl/products/pyxser/
# http://xmpppy.sourceforge.net/ 
# have to send the 'view' object on modified to clients
# use the pyxser library to serialize the 'view' object on both ends
# http://coder.cl/products/pyxser/


class SeamlessCommand(sublime_plugin.EventListener):
        
        Send_data = 0
        Recv_data = 0

        def on_load(self, view):                
                print 'thread runnin'
                print self.Recv_data, 'printing'
                thread.start_new_thread(self.update, (view,''))

        def on_modified(self, view):

                reg = sublime.Region(0, 10000)
                self.Send_data = str(view.substr(reg))
                print self.Send_data
                #print view.sel()
                print "onmod recv", self.Recv_data
                self.update(view, '')

        def on_post_save(self, view):
                #print "on_save called"
                self.Recv_data = "apples"
                print self.Recv_data


        def update(self, view, string):
                print "recv", self.Recv_data
                while(self.Recv_data != 0):
                        edit = view.begin_edit()
                        view.insert(edit, 0, self.Recv_data)
                        self.Recv_data = 0

