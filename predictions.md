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


