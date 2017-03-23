import zmq
import time
import json
import logging
import sys


class module(object):


    def __init__(self, mod_name, config):

        self.context = zmq.Context()
        self.config = config
        logging.basicConfig(format='%(asctime)s %(message)s', filename='log/module.log', level=logging.INFO)
        self.name = mod_name
        self.identity = self.config[mod_name]['identity']
        self.url_control = self.config[mod_name]['url']
        self.socket_control = self.context.socket(zmq.DEALER)
        self.establish_connection()
        self.poller = zmq.Poller()
        self.poller.register(self.socket_control, zmq.POLLIN)


    def establish_connection(self):

        self.socket_control.connect(self.url_control)
        self.sysout('established connection')


    def send(self, MESSAGE):

        self.socket_control.send_multipart(MESSAGE)
        self.sysout('send message', MESSAGE)


    def receive(self):

        MESSAGE = self.socket_control.recv_multipart()
        self.sysout('receive message', MESSAGE)

        return MESSAGE


    def extract_core(self, MESSAGE):
        CORE = MESSAGE[-1]
        CORE_json = CORE.decode('ascii')
        CORE_pyobj = json.loads(CORE_json)
        return CORE_pyobj


    def create_message(self, TO = 'X', CORE = "no input"):

        if type(TO) is str:
            FROM = [self.identity]
            CORE_json = json.dumps(CORE)
            CORE_bytes = [CORE_json.encode('ascii')]
            ADDRESS = []
            TO = [self.config[TO]['identity']]

        elif type(TO) is list:
            MESSAGE_received = TO
            FROM = [self.identity]
            CORE_json = json.dumps(CORE)
            CORE_bytes = [CORE_json.encode('ascii')]
            MESSAGE_received.pop()
            TO = [MESSAGE_received.pop()]
            MESSAGE_received.pop()
            ADDRESS = MESSAGE_received

        MESSAGE = ADDRESS + TO + FROM + CORE_bytes
        return MESSAGE


    def sysout(self, action, meta=False):

        sys.stdout.write('\n'+'<> {}   #'.format(self.name)+str(action)+'\n'+'['+str(self.socket_control)+']'+'\n'+'{}'.format(str(meta)+'\n' if meta else '')+'</>'+'\n')


        sys.stdout.flush()


        logging.info('\n<> {}   #{}\n   [{}]\n   {}\n</>'.format(self.name, str(action), str(self.socket_control),     str(meta) if meta else ''))


    def destroy(self):
        self.context.destroy()
