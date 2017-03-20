import json

from structure.configuration import config
from structure.module import module



def main():

    remote_maintenance = module('API_MAINTENANCE', config)


    while True:
        try:

            MESSAGE = remote_maintenance.receive()
            CORE_pyobj = remote_maintenance.extract_core(MESSAGE)


            request = CORE_pyobj["request"]

            if request == "run maintenance protocol A1":

                response = "the maintenance protocol was successfully completed"

            elif request == "run maintenance protocol C3":

                MESSAGE_2 = remote_maintenance.create_message(TO = b'database', CORE_pyobj = {"request":"school"})
                remote_maintenance.send(MESSAGE_2)

                MESSAGE_2 = remote_maintenance.receive()

                response = remote_maintenance.extract_core(MESSAGE_2)


            MESSAGE = remote_maintenance.create_message(CORE_pyobj = {request : response}, MESSAGE_received = MESSAGE)
            remote_maintenance.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
