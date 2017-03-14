from multiprocessing import Process

from structure import config
from structure import broker



def main():

    control_broker = broker.entity(config.data)
    control_broker.mediate()



if __name__ == '__main__':
    main()
