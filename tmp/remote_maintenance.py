
import time
import zmq
import json



def main():

    context = zmq.Context()
    socket_prog_infiloop = context.socket(zmq.REP)
    socket_prog_infiloop.bind("tcp://127.0.0.1:6666")
    poller = zmq.Poller()
    poller.register(socket_prog_infiloop, zmq.POLLIN)

    count = 0

    while True:
        try:
            sockets = dict(poller.poll(10))
            if socket_prog_infiloop in sockets:

                address, zmq_input = socket_prog_infiloop.recv_multipart()
                json_input = zmq_input.decode('ascii')
                pyobj_input = json.loads(json_input)

                payload = pyobj_input["payload"]

                # print to console
                print('\n {{\n       >>>>> program recieve\n       # name: prog_infiloop\n       # payload: {}\n     }}\n'.format(payload))

                pyobj_output = {"result" : count}
                json_output = json.dumps(pyobj_output)
                zmq_output = json_output.encode('ascii')

                socket_prog_infiloop.send_multipart([address, zmq_output])

            count += 1
            time.sleep(1)
            print(count)



        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
