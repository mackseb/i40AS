import json
from random import randint
import time

from structure.configuration import config
from structure.module import module



def main():

    interface = module('INTERFACE', config)
    count = 0

    while True:
        try:
            sockets = dict(interface.poller.poll(10))
            if interface.socket_control in sockets:

                MESSAGE = interface.receive()
                CORE_pyobj = interface.extract_core(MESSAGE)

                print(CORE_pyobj)
                request = CORE_pyobj["request"]


                MESSAGE = interface.create_message(CORE_pyobj = {"current position" : response, "current loop": count}, MESSAGE_received = MESSAGE )
                interface.send(MESSAGE)


            count += 1
            response = "{}°".format(randint(0,360))
            time.sleep(2)
            print(count)


        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    main()
