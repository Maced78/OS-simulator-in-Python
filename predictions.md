## Part A - Investigating my system
Date: 2026-11-26, before running any command

My guess: approximately 200 processes.
Why: I mainly use Windows, so not many programs run on my Ubuntu, but there are
system processes, the terminal, and the browser's processes (and its tabs).


## Part B2 – Race condition (written before the code)

**Q1. Six sensors each add 1 to a shared counter 305 times, without a lock. What will the final value be: exactly 1830, less, or more? Why?**

My prediction: Each sensor has 305 so the value will multiplied by 6 and the result will be around 1830 

**Q2. Will all 5 runs without the lock give the same value? Why?**

My prediction: I think the 5 runs will not give the same value, because some increments can be lost.

**Q3. With a Lock, what will the final value be?**

My prediction: With a Lock, I think the final value will be the similar to without lock, because only one sensor can change the counter at a time, but it would be exactly 1830.

**Q4. Will the version with the Lock be faster or slower than the version without it? Why?**

My prediction: I think the Lock version will be slower, because the sensors have to wait.

Result:

The actual results mostly matched my predictions. Without a Lock, the counter values were sometimes different because simultaneous increments could be lost, while with a Lock, all five runs produced exactly 1830; the Lock version was also slightly slower because processes had to wait for access to the shared counter.

## Part B3 – Watchdog (written before the code)

**Q1. Will the restarted sensor 2 have the same PID as the crashed one? Why?**

My prediction: I think the PID will change, because it will be a new process.

**Q2. Who will be the parent (PPID) of the restarted sensor 2?**

My prediction: I think the parent will be forkserver, because in B1 we observed similar situation.

**Q3. What exit code will the crashed sensor have, compared to a normal sensor?**

My prediction: I think the crashed sensor will have non-zero, while a normal one has zero, because it raises an exception.

**Q4. How many lines will field.log have at the end? Why?**

My prediction: I think field.log will have still 1830 lines, because the restarted sensor 2 will continue from the next reading.
