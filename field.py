import os
from multiprocessing import Process
import multiprocessing
def sensor(n):
	print("Number of process: ",n, "PID: ", os.getpid(), "PPID: ", os.getppid())

if __name__ == "__main__":
    procs = []
    for n in range(1, 7):
        p = Process(target=sensor, args=(n,))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
    print("main PID:", os.getpid(), "- all sensors finished")
    print(multiprocessing.get_start_method())
