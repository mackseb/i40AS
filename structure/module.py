import zmq
import time
import json
import logging
import sys


class entity(object):



    def __init__(self, key, info):

        self.context = zmq.Context()
        self.info = info
        logging.basicConfig(format='%(asctime)s %(message)s', filename='log/module.log', level=logging.INFO)
        self.identity = self.info[key]['identity']
        self.url_control = self.info[key]['url']
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


    def create_message(self, TO = b'someone', CORE_pyobj = "no input", MESSAGE_received = False):

        ADDRESS = []
        TO = [TO]
        FROM = [self.identity]
        CORE_json = json.dumps(CORE_pyobj)
        CORE = [CORE_json.encode('ascii')]

        if MESSAGE_received:

            MESSAGE_received.pop()
            TO = [MESSAGE_received.pop()]
            MESSAGE_received.pop()
            ADDRESS = MESSAGE_received


        MESSAGE = ADDRESS + TO + FROM + CORE
        return MESSAGE


    def sysout(self, action, meta=False):

        sys.stdout.write('\n')
        sys.stdout.write('<> {}   #'.format(self.identity))
        sys.stdout.write(str(action))
        sys.stdout.write('\n')
        sys.stdout.write('[')
        sys.stdout.write(str(self.socket_control))
        sys.stdout.write(']')
        sys.stdout.write('\n')

        if meta:

            sys.stdout.write(str(meta))
            sys.stdout.write('\n')

        sys.stdout.write('</>')
        sys.stdout.write('\n')
        sys.stdout.flush()


        logging.info('\n<> {}   #{}\n   [{}]\n   {}\n</>'.format(self.identity, str(action), str(self.socket_control),     str(meta) if meta else ''))


    def destroy(self):
        self.context.destroy()
