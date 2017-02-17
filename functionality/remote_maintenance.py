import json

from structure import structure_module



def main(name, info):

    remote_maintenance = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = remote_maintenance.receive()

            CORE_pyobj = remote_maintenance.extract_core(MESSAGE)



            payload = CORE_pyobj["payload"]

            if payload == "warte irgendwas":

                result = "ich habe etwas gewartet"

            elif payload == "checke datenhistory":

                MESSAGE_2 = remote_maintenance.create_message(TO = b'database', CORE_pyobj = {"payload":"school"})
                remote_maintenance.send(MESSAGE_2)

                MESSAGE_2 = remote_maintenance.receive()

                result = {"datenhistory" :  remote_maintenance.extract_core(MESSAGE_2)}

            MESSAGE = remote_maintenance.create_message(CORE_pyobj = result, MESSAGE_received = MESSAGE)

            remote_maintenance.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
