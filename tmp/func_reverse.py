import time
import random


def main(pyobj_input):

    data = pyobj_input
    payload = data["payload"]
    simulated_time = data["simulated_time"]
    chaotic = data["chaotic"]

    reversed_string_list = []
    t0 = time.clock()
    if chaotic:
        random_workload = random.randint(1,1000)
    else:
        random_workload = 0

    for i in payload:
        reversed_string_list.append(i[::-1])


    # simulate processing time
    time.sleep(simulated_time+(random_workload/1000))

    process_time = time.clock() - t0

    pyobj_output = {"result" : reversed_string_list, "process_time" : process_time}


    return pyobj_output



if __name__ == "__main__":
    print(main({"payload":["Hallo Welt", "Batman", "TU Darmstadt"],"simulated_time": 2, "chaotic": False}))
