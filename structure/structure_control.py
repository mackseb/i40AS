import sys
import zmq
import logging


class entity(object):


    def __init__(self, info):

        self.context = zmq.Context()
        self.info = info
        logging.basicConfig(format='%(asctime)s %(message)s', filename='log/control.log', level=logging.INFO)

        self.url_client = self.info['client']['url']
        self.socket_client = self.context.socket(zmq.ROUTER)
        self.info['client']['socket'] = self.socket_client
        self.socket_client.bind(self.url_client)


        for key in self.info:
            if key != 'client':
                exec('self.url_' + key + '=' + 'self.info[key][\'url\']')
                exec('self.socket_' + key + '=' + 'self.context.socket(zmq.DEALER)')
                exec('self.info[key][\'socket\']' + '=' + 'self.socket_' + key)
                exec('self.socket_' + key + '.bind' + '(self.url_' + key + ')' )


        self.poller = zmq.Poller()
        for key in info:
            exec('self.poller.register(self.socket_' + key + ', zmq.POLLIN)')


        for key in self.info:
            self.sysout('established socket', meta=self.info[key])


    def mediate(self):
        count = 0
        while True:
            try:
                self.sysout('completed loop', meta= count)
                sockets = dict(self.poller.poll())

                for key in self.info:

                    if sockets.get(self.info[key]['socket']) == zmq.POLLIN:

                        MESSAGE = self.info[key]['socket'].recv_multipart()
                        self.sysout('received message', current_socket=self.info[key]['socket'], meta = MESSAGE)

                        TO = MESSAGE[-3]

                        for key in self.info:
                            if TO == self.info[key]['identity']:

                                self.info[key]['socket'].send_multipart(MESSAGE)
                                self.sysout('send message', current_socket=self.info[key]['socket'], meta = MESSAGE)
                count += 1

            except KeyboardInterrupt:
                break


    def sysout(self, action, current_socket=False, meta=False):

        sys.stdout.write('\n')
        sys.stdout.write('<> control   #')
        sys.stdout.write(str(action))
        if current_socket:
            sys.stdout.write('\n')
            sys.stdout.write('[')
            sys.stdout.write(str(current_socket))
            sys.stdout.write(']')
        sys.stdout.write('\n')

        if meta:

            sys.stdout.write(str(meta))
            sys.stdout.write('\n')

        sys.stdout.write('</>')
        sys.stdout.write('\n')
        sys.stdout.flush()


        logging.info('\n<> control   #{}\n   [{}]\n   {}\n</>'.format(str(action), str(current_socket) if current_socket else '', str(meta) if meta else ''))


    def destroy(self):
        self.socket.close()
        self.context.destroy()
