import json
import pandas
import time
from structure import structure_client



def main(info):

    shell_client = structure_client.entity(info)

    MESSAGE = shell_client.create_message(TO = b'IO_asset', CORE_pyobj = {"payload":"bewege dich irgendwie"})


    count = 1
    while True:
        try:
            shell_client.send(MESSAGE)
            print(shell_client.extract_core(shell_client.receive()))
            print(count)
            count += 1
            time.sleep(2)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
