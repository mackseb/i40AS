import json

from structure import structure_module



def main(name, info):

    shell_communication = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = shell_communication.receive()

            CORE_pyobj = shell_communication.extract_core(MESSAGE)



            payload = CORE_pyobj["payload"]

            result = "ICH schicke eine http Anfrage"

            MESSAGE = shell_communication.create_message(CORE_pyobj = {payload : result}, MESSAGE_received = MESSAGE )

            shell_communication.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
