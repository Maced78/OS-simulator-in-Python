from itertools import count
import os
from multiprocessing import Process, Queue
import multiprocessing
import random
import time

SENSORS = 6              
READINGS = 305
INTERVAL = 0.018
STUDENT_ID = 240108021


def sensor(n,q):
    print("Sensors: ", n, "PID: ", os.getpid(), "PPID: ", os.getppid())

    rng = random.Random(STUDENT_ID + n)
    for i in range(READINGS):
        time.sleep(INTERVAL)
        reading = rng.randint(150, 350)
        if i < 3:
            print(f"Sensor {n} - Reading {i + 1}: {reading}")
        q.put((n, os.getpid(), time.time(), i + 1, reading))
    q.put("STOP")
    



def logger(q):
    print("Logger PID: ", os.getpid(), "PPID: ", os.getppid())
    os.makedirs("logs", exist_ok=True)  
    count = 0
    stops = 0
    with open("logs/field.log", "w") as f:   
        while True:
                item = q.get()          
                if item == "STOP":
                    stops += 1
                    if stops == SENSORS:
                        break
                else:
                    f.write(f"{item}\n") 
                    count += 1

    print("wrote", count, "lines")

    


if __name__ == "__main__":
    start = time.time()
    procs = []
    q = Queue()

    p2 = Process(target=logger, args=(q,))
    p2.start()
    procs.append(p2)
    for n in range(1, SENSORS + 1):
        p1 = Process(target=sensor, args=(n,q))
        p1.start()
        
        procs.append(p1)
        
    for p in procs:
        p.join()
    print("main PID:", os.getpid(), "- all sensors finished")
    print(multiprocessing.get_start_method())
    print("Total time:", time.time() - start)



