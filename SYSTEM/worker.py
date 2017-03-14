import json

from structure import structure_module

from SYSTEM import sys_function_A
from SYSTEM import sys_function_B
from SYSTEM import sys_function_C



def main(name, info):

    system_module = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = system_module.receive()
            CORE_pyobj = system_module.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            if request == 'A':
                sys_function_A.main()
            elif request == 'B':
                sys_function_B.main()
            elif request == 'C':
                sys_function_C.main()

            response = "function has been executed"


            MESSAGE = system_module.create_message(CORE_pyobj = {request : response}, MESSAGE_received = MESSAGE )
            system_module.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
