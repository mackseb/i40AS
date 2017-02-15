import zmq



class entity(object):



    def __init__(self, url_client, url_database):

        self.context = zmq.Context()

        self.url_client = url_client
        self.url_database = url_database

        self.socket_client = self.context.socket(zmq.ROUTER)
        self.socket_client.bind(self.url_client)
        self.socket_database = self.context.socket(zmq.DEALER)
        self.socket_database.bind(self.url_database)

        self.poller = zmq.Poller()
        self.poller.register(self.socket_client, zmq.POLLIN)
        self.poller.register(self.socket_database, zmq.POLLIN)



    def mediate(self):

        while True:

            sockets = dict(self.poller.poll())

            if sockets.get(self.socket_client) == zmq.POLLIN:

                address, entity, CORE_zmq = self.socket_client.recv_multipart()
                print(address)
                print(entity)
                print(CORE_zmq)

                if entity == b'database':

                    self.socket_database.send_multipart([address, CORE_zmq])



            if sockets.get(self.socket_database) == zmq.POLLIN:

                address, CORE_zmq = self.socket_database.recv_multipart()
                self.socket_client.send_multipart([address, CORE_zmq])



    def destroy(self):
        self.socket.close()
        self.context.destroy()
