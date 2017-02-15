import zmq
import time
import zmq
import json



class entity(object):



    def __init__(self, url):

        self.context = zmq.Context()
        self.url_control = url
        self.socket_control = self.context.socket(zmq.DEALER)
        self.establish_connection()



    def establish_connection(self):

        self.socket_control.connect(self.url_control)



    def send_request(self, ENTITY_zmq, CORE_zmq):

        self.socket_control.send_multipart([ENTITY_zmq, CORE_zmq])



    def receive_response(self):

        CORE_zmq = self.socket_control.recv_multipart()

        return CORE_zmq



    def destroy(self):
        self.context.destroy()
