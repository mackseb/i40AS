import json
import pandas

from structure import structure_module



def main(name, info):

    shell_database = structure_module.entity(name, info)

    data = pandas.read_csv("database/data.csv")


    while True:
        try:

            MESSAGE = shell_database.receive()
            CORE_pyobj = shell_database.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            response = data[request].to_dict()
            for key in response:
                response = str(response)


            MESSAGE = shell_database.create_message(CORE_pyobj = {request : response}, MESSAGE_received = MESSAGE )
            shell_database.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
