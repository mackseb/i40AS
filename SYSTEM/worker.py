import json

from structure.configuration import config
from structure.module import module

from SYSTEM import sys_function_A
from SYSTEM import sys_function_B
from SYSTEM import sys_function_C



def main():

    system = module('SYSTEM', config)


    while True:
        try:

            MESSAGE = system.receive()
            CORE_pyobj = system.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            if request == 'A':
                sys_function_A.main()
            elif request == 'B':
                sys_function_B.main()
            elif request == 'C':
                sys_function_C.main()

            response = "function has been executed"


            MESSAGE = system.create_message(CORE_pyobj = {request : response}, MESSAGE_received = MESSAGE )
            system.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
