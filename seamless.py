import sublime, sublime_plugin
from time import sleep
import os, sys
import socket
from threading import Thread

class SeamlessCommand(sublime_plugin.EventListener):
        
        Send_data = 0
        Recv_data = 0
        send_path = "/tmp/seamless-send"
        recv_path = "/tmp/seamless-recv"
        client = ''
        server = ''


        def on_load(self, view):              
                print 'on_load'
                self.client = self.start_sendIPC()
                #t = Thread(target = self.start_recvIPC(), args=(self, ''))
                self.server = self.start_recvIPC()
                print self.server
                self.server.settimeout(0.0)

        def on_modified(self, view):

                reg = sublime.Region(0, 10000)
                self.Send_data = str(view.substr(reg))
                print self.Send_data
                self.client.send(self.Send_data)
                self.update(view, '')

                
        def on_post_save(self, view):
                #print "on_save called"
                self.Recv_data = "apples"
                #print self.Recv_data


        def update(self, view, string):
                print "recv", self.Recv_data
               #print datagram
                datagram = self.server.recv(1024)
                if datagram :
                        edit = view.begin_edit()
                        view.insert(edit, 0, datagram)
                        self.Recv_data = 0
                        view.end_edit(edit)

        def start_sendIPC(self):
                if os.path.exists(self.send_path):
                        client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
                        client.connect(self.send_path)
                        print "send connected"
                        return client
                else:
                        print "path doesnt exist, creating"

        def start_recvIPC(self):
                if os.path.exists(self.recv_path):
                        os.remove(self.recv_path)
                server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
                server.bind(self.recv_path)
                print "recv connected"
                return server

                                       
