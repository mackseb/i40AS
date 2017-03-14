import json
import pandas

from structure import structure_module



def main(name, info):

    database_module = structure_module.entity(name, info)

    data = pandas.read_csv("database/data.csv")


    while True:
        try:

            MESSAGE = database_module.receive()
            CORE_pyobj = database_module.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            response = data[request].to_dict()
            for key in response:
                response = str(response)


            MESSAGE = database_module.create_message(CORE_pyobj = {request : response}, MESSAGE_received = MESSAGE )
            database_module.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
