# Part A answers

## Q1
Processes: 470 (ps -e | wc -l, minus the header)
Shell threads: 1 
Running services: 35
Last boot: 2026-11-26 15:24:14 (uptime -s)
Comparison with my prediction (200): 470

## Q2
Chain when run directly: systemd(1) → systemd(5152) → ptyxis(17149) → ptyxis-agent(17169) → bash(17216) → python3 sysinfo.py(25617)

Chain when run from run_sysinfo.py: systemd(1) → systemd(5152) → ptyxis(17149) → ptyxis-agent(17169) → bash(17216) 
→ python3 run_sysinfo.py(25797) → python3 sysinfo.py(25803)

What changed: The parent of python3 sysinfo.py , from bash to python3 run_sysinfo.py. 
The chain become longer, the PID can be different on every try because every run is a new process. 

## Q3
1) root  1  0.0  0.0  26816 16756 ?  Ss  12:18  0:01 /usr/lib/systemd/systemd --switched-root --system --deserialize=57 splash

Definition: PID is 1 , Ss means two thing; Capital S is interruptible sleep: Process is paused or waiting,
second s is session leader: the first process of the session. It mostly has nothing to do, so it sleeps and waits for a process to start.

2) root           5  0.0  0.0      0     0 ?        I<   12:18   0:00 [kworker/R-sync_wq]

Definition: PID is 5, I< got two parts ; I is idle kernel thread, introduced in Linux 4.14, < means high priority.
In this process resident and virtual memories are both zero, because kernel-threads has no user-space address space.
It is idle right now, and its mission is to wait until kernel gives it a job.

3) akeo       10849  0.0  0.0  12636  4864 pts/0    R+   14:00   0:00 ps aux

Definition: PID is 10849, R+ means; R -> the process is currently running, + means foreground process group. 
It's a userspace process so it has virtual memory of 12636 KiB, and 4864 KiB resident memory, it has no brackets because 
it was started from a program file (/usr/bin/ps) with a command line.
