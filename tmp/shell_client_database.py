import json
import pandas
import time
from structure import structure_client



def main(info):

    shell_client = structure_client.entity(info)

    MESSAGE = shell_client.create_message(TO = b'database', CORE_pyobj = {"payload":"school"})


    count = 1
    while True:
        try:
            shell_client.send(MESSAGE)
            shell_client.receive()
            print(count)
            count += 1
            time.sleep(8)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
