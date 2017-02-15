import json
import time

from client_entity import client



def main(entity = b'database', CORE_json = json.dumps({"payload": "school"})):


    initialized_client = client()

    count = 1

    while True:
        try:
            initialized_client.send(entity, CORE_json)

            CORE_json = initialized_client.receive()

            print(CORE_json)
            print(count)

            count += 1
            time.sleep(2)


        except KeyboardInterrupt:
            break



if __name__ == '__main__':
    main()
