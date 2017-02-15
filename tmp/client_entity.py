import json
import zmq



class client(object):


    def __init__(self):

        self.context = zmq.Context()
        self.url_control = "tcp://127.0.0.1:5555"
        self.socket_control = self.context.socket(zmq.DEALER)


        self.establish_connection()



    def establish_connection(self):

        self.socket_control.connect(self.url_control)



    def send(self, entity, CORE_json):

        CORE_zmq = CORE_json.encode('ascii')
        self.socket_control.send_multipart([entity, CORE_zmq])



    def receive(self):

        CORE_zmq = self.socket_control.recv_multipart()
        CORE_json = CORE_zmq[0].decode('ascii')

        return CORE_json



    def destroy(self):
        self.context.destroy()
