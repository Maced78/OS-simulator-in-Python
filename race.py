from itertools import count
import os
from multiprocessing import Process, Queue, Value, Lock
import multiprocessing
import random
import time

SENSORS = 6
READINGS = 305
INTERVAL = 0
STUDENT_ID = 240108021
RUNS = 5


def sensor(n, q, counter, lock=None):

    rng = random.Random(STUDENT_ID + n)

    for i in range(READINGS):

        time.sleep(INTERVAL)

        reading = rng.randint(150, 350)

        if lock is None:
            counter.value += 1
        else:
            with lock:
                counter.value += 1

        if i == 0:
            print(
                f"Sensor {n}, PID: {os.getpid()}, "
                f"First reading: {reading}"
            )

        q.put((
            n,
            os.getpid(),
            time.time(),
            i + 1,
            reading
        ))

    q.put("STOP")


def logger(q, run_number, mode):

    os.makedirs("logs", exist_ok=True)

    count = 0
    stops = 0

    filename = f"logs/field_{mode}_{run_number}.log"

    with open(filename, "w") as f:

        while stops < SENSORS:

            item = q.get()

            if item == "STOP":
                stops += 1
            else:
                f.write(f"{item}\n")
                count += 1

    print("wrote", count, "lines")


def run_experiment(use_lock, run_number):

    counter = Value("i", 0, lock=False)

    lock = Lock() if use_lock else None

    q = Queue()

    mode = "safe" if use_lock else "unsafe"

    logger_process = Process(
        target=logger,
        args=(q, run_number, mode)
    )

    logger_process.start()

    processes = []

    start = time.perf_counter()

    for n in range(1, SENSORS + 1):

        p = Process(
            target=sensor,
            args=(n, q, counter, lock)
        )

        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    elapsed = time.perf_counter() - start

    logger_process.join()

    q.close()
    q.join_thread()

    return counter.value, elapsed


if __name__ == "__main__":

    print("Multiprocessing start method:",
      multiprocessing.get_start_method())

    print("\n========== B2: WITHOUT LOCK ==========")

    no_lock_results = []

    for run in range(1, RUNS + 1):

        result, elapsed = run_experiment(False, run)

        no_lock_results.append((result, elapsed))

        print(
            f"Run {run}: Counter = {result}, "
            f"Time = {elapsed:.4f} seconds"
        )

    print("\n========== B2: WITH LOCK ==========")

    lock_results = []

    for run in range(1, RUNS + 1):

        result, elapsed = run_experiment(True, run)

        lock_results.append((result, elapsed))

        print(
            f"Run {run}: Counter = {result}, "
            f"Time = {elapsed:.4f} seconds"
        )

    avg_without = sum(
        t for _, t in no_lock_results
    ) / RUNS

    avg_with = sum(
        t for _, t in lock_results
    ) / RUNS

    print("\n========== FINAL RESULTS ==========")

    print("Expected counter:", SENSORS * READINGS)

    print(f"Average without Lock: {avg_without:.4f} seconds")
    print(f"Average with Lock:    {avg_with:.4f} seconds")