import json

from structure import structure_module



def main(name, info):

    shell_IO_asset = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = shell_IO_asset.receive()

            CORE_pyobj = shell_IO_asset.extract_core(MESSAGE)



            payload = CORE_pyobj["payload"]

            result = "ICH fahre nach links rechts unten"

            MESSAGE = shell_IO_asset.create_message(CORE_pyobj = {payload : result}, MESSAGE_received = MESSAGE )
            print(MESSAGE)
            shell_IO_asset.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
