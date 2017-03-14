import json
from random import randint
from structure import structure_module
import time


def main(name, info):

    interface_module = structure_module.entity(name, info)
    count = 0

    while True:
        try:
            sockets = dict(interface_module.poller.poll(10))
            if interface_module.socket_control in sockets:

                MESSAGE = interface_module.receive()
                CORE_pyobj = interface_module.extract_core(MESSAGE)

                print(CORE_pyobj)
                request = CORE_pyobj["request"]


                MESSAGE = interface_module.create_message(CORE_pyobj = {"current position" : response, "current loop": count}, MESSAGE_received = MESSAGE )
                interface_module.send(MESSAGE)


            count += 1
            response = "{}°".format(randint(0,360))
            time.sleep(2)
            print(count)


        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    main()
