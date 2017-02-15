
import logging
import zmq
import json

from helper import sysout

from functionality import func_reverse


class worker(object):


    def __init__(self, identity):

        self.context = zmq.Context()
        self.identity = identity
        self.url_backend = "tcp://127.0.0.1:5556"
        self.url_prog_infiloop = "tcp://127.0.0.1:6666"
        self.url_database =  "tcp://127.0.0.1:7777"
        self.socket_backend = self.context.socket(zmq.DEALER)
        self.socket_prog_infiloop = self.context.socket(zmq.REQ)
        self.socket_database = self.context.socket(zmq.REQ)
        self.establish_connection()


        # set up log file
        logging.basicConfig(format='%(asctime)s %(message)s', filename='zeromq_IO/log/backend.log', level=logging.INFO)
        # add to log
        logging.info('\n {{\n       +++++ initialized zmq worker\n        # ID: {} \n       }}'.format(self.identity))
        # print to console
        sysout.main('\n {{\n       +++++ initialized zmq worker\n       # ID: {} \n       }}'.format(self.identity))


    def establish_connection(self):

        self.socket_backend.connect(self.url_backend)
        self.socket_prog_infiloop.connect(self.url_prog_infiloop)
        self.socket_database.connect(self.url_database)


    def routine(self):

        while True:

            address, zmq_input = self.socket_backend.recv_multipart()

            json_input = zmq_input.decode('ascii')
            pyobj_input = json.loads(json_input)

            pyobj_output = func_reverse.main(pyobj_input)
            json_output = json.dumps(pyobj_output)
            zmq_output = json_output.encode('ascii')


            self.socket_backend.send_multipart([address, zmq_output])


            """
            elif functionality == b'func_google_location':

                json_input = zmq_input.decode('ascii')


                json_output = func_google_location.main(json_input)
                zmq_output = json_output.encode('ascii')
                self.socket_backend.send_multipart([address, zmq_output])


            elif functionality == b'prog_infiloop':

                self.socket_prog_infiloop.send_multipart([address, zmq_input])

                address, zmq_output = self.socket_prog_infiloop.recv_multipart()


                self.socket_backend.send_multipart([address, zmq_output])


            elif functionality == b'database':

                self.socket_database.send_multipart([address, zmq_input])

                address, zmq_output = self.socket_database.recv_multipart()


                self.socket_backend.send_multipart([address, zmq_output])

            else:

                self.socket_backend.send_multipart([b"ERROR"])
            """




    def destroy(self):
        self.context.destroy()


def main(identity):

    initialized_worker = worker(identity)
    initialized_worker.routine()
