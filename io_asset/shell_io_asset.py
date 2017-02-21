import json
from random import randint
from structure import structure_module
import time


def main(name, info):

    shell_io_asset = structure_module.entity(name, info)
    count = 0

    while True:
        try:
            sockets = dict(shell_io_asset.poller.poll(10))
            if shell_io_asset.socket_control in sockets:

                MESSAGE = shell_io_asset.receive()
                CORE_pyobj = shell_io_asset.extract_core(MESSAGE)

                print(CORE_pyobj)
                request = CORE_pyobj["request"]


                MESSAGE = shell_io_asset.create_message(CORE_pyobj = {"current position" : response, "current loop": count}, MESSAGE_received = MESSAGE )
                shell_io_asset.send(MESSAGE)


            count += 1
            response = "{}°".format(randint(0,360))
            time.sleep(2)
            print(count)


        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    main()
