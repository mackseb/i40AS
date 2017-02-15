
import zmq
import time
import zmq
import json
import pandas as pd



class database(object):



    def __init__(self):

        self.context = zmq.Context()
        self.url_control = "tcp://127.0.0.1:5556"
        self.socket_control = self.context.socket(zmq.DEALER)
        self.establish_connection()

        self.data = pd.read_csv("database_shell.csv")



    def establish_connection(self):

        self.socket_control.connect(self.url_control)



    def send_socket_control(self, address, CORE_zmq):

        self.socket_control.send_multipart([address, CORE_zmq])



    def receive_socket_control(self):

        address, CORE_zmq = self.socket_control.recv_multipart()

        return (address, CORE_zmq)



    def destroy(self):
        self.context.destroy()
