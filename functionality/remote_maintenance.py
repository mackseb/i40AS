import json

from structure import structure_module



def main(name, info):

    remote_maintenance = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = remote_maintenance.receive()

            CORE_pyobj = remote_maintenance.extract_core(MESSAGE)



            payload = CORE_pyobj["payload"]

            result = "ich habe etwas gewartet"

            MESSAGE = remote_maintenance.create_message(CORE_pyobj = {payload : result}, MESSAGE_received = MESSAGE )

            remote_maintenance.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
