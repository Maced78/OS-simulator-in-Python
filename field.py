import os
from multiprocessing import Process
import multiprocessing
import random
import time

SENSORS = 6              
READINGS = 305
INTERVAL = 0.018
STUDENT_ID = 240108021


def sensor(n):
    print("Number of process: ", n, "PID: ", os.getpid(), "PPID: ", os.getppid())

    rng = random.Random(STUDENT_ID + n)
    for i in range(READINGS):
        time.sleep(INTERVAL)
        reading = rng.randint(150, 350)
        if i < 3:
            print(f"Sensor {n} - Reading {i + 1}: {reading}")


if __name__ == "__main__":
    procs = []
    for n in range(1, SENSORS + 1):
        p = Process(target=sensor, args=(n,))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
    print("main PID:", os.getpid(), "- all sensors finished")
    print(multiprocessing.get_start_method())



