
from database_entity import database
import json


def main():

    database_shell = database()

    while True:
        try:

            address, CORE_zmq = database_shell.receive_socket_control()
            CORE_json = CORE_zmq.decode('ascii')
            CORE_pyobj = json.loads(CORE_json)


            payload = CORE_pyobj["payload"]
            result = database_shell.data[payload].to_dict()
            for key in result:
                result = str(result)


            CORE_pyobj = {payload : result}
            CORE_json = json.dumps(CORE_pyobj)
            CORE_zmq = CORE_json.encode('ascii')

            database_shell.send_socket_control(address, CORE_zmq)





        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
