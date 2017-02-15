import zmq

from structure import structure_control



def main(info):

    shell_control = structure_control.entity(info)
    shell_control.mediate()
