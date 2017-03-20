import json
import pandas

from structure.configuration import config
from structure.module import module



def main():

    database = module('DATABASE', config)

    db_pandas = pandas.read_csv("database/data.csv")


    while True:
        try:

            MESSAGE = database.receive()
            CORE_pyobj = database.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            response = db_pandas[request].to_dict()
            for key in response:
                response = str(response)


            MESSAGE = database.create_message(CORE_pyobj = {request : response}, MESSAGE_received = MESSAGE )
            database.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
