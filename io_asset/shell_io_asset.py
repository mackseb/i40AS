import json

from structure import structure_module



def main(name, info):

    shell_io_asset = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = shell_io_asset.receive()

            CORE_pyobj = shell_io_asset.extract_core(MESSAGE)



            payload = CORE_pyobj["payload"]

            result = "ICH fahre nach links dann nach oben"

            MESSAGE = shell_io_asset.create_message(CORE_pyobj = {payload : result}, MESSAGE_received = MESSAGE )

            shell_io_asset.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
