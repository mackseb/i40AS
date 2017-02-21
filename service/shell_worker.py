import json

from structure import structure_module

from service import sys_function_A
from service import sys_function_B
from service import sys_function_C



def main(name, info):

    shell_worker = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = shell_worker.receive()
            CORE_pyobj = shell_worker.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            if request == 'A':
                sys_function_A.main()
            elif request == 'B':
                sys_function_B.main()
            elif request == 'C':
                sys_function_C.main()

            response = "function has been executed"


            MESSAGE = shell_worker.create_message(CORE_pyobj = {request : response}, MESSAGE_received = MESSAGE )
            shell_worker.send(MESSAGE)


        except KeyboardInterrupt:
            break





if __name__ == "__main__":
    main()
