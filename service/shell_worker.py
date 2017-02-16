import json

from structure import structure_module



def main(name, info):

    shell_worker = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = shell_worker.receive()

            CORE_pyobj = shell_worker.extract_core(MESSAGE)



            payload = CORE_pyobj["payload"]

            result = "ICH habe eine funktion aufgerufen"

            MESSAGE = shell_worker.create_message(CORE_pyobj = {payload : result}, MESSAGE_received = MESSAGE )

            shell_worker.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
