import zmq

from structure import structure_control



def main(info):

    control_broker = structure_control.entity(info)
    control_broker.mediate()


if __name__ == "__main__":
    main()
