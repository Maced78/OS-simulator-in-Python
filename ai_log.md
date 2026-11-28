Note: Day 1 and Day 2 entries were written late (on 28.11) with Claude's help, using the chat history as a record.

## Day 1 – 26.11.2026
- Asked Claude what the task is about and how to plan it over the week.

- Asked about git errors (`git commit m-`, empty README, `>` vs `>>`). Claude explained the correct commands.

- Asked what some Linux commands and outputs mean (ps -e, top, /proc/$$/status, fd 255, uptime -s, who -b, pstree, systemctl). Claude explained them; I ran the commands and wrote the answers myself.
- Asked how a for loop over PATH works and why my sysinfo.py gave NameError and SyntaxError. Claude explained the errors; I fixed the code.
- Asked why subprocess.run(["sysinfo.py"]) didn't work. Claude explained that it needs ["python3", "sysinfo.py"].

## Day 2 – 27.11.2026
- Asked what ps state codes mean (Ss, I<, R+, Sl) for Q3. Claude explained the letters; I wrote my own answers.

- Asked how to start field.py (processes, seed, queue, logger). Claude explained the concepts with general examples; I wrote the code.
- Asked about many errors in field.py: tabs vs spaces (TabError), only 5 sensors from range(1,6), a generator printed instead of a value, q not passed to the processes, 6 loggers created in the loop, p2.start() called twice, STOP lines written to the log, the logger loop structure. Claude pointed out the cause of each error; I fixed them.
- Asked why the sensors' parent is forkserver and not main. Claude explained Python's start method on Linux.
- Asked whether my ps screenshot was correct and what Sl means. Claude explained the Queue feeder thread.
- Asked why `grep -c 19875` gave 306 and not 305. Claude explained that grep also matched digits inside a timestamp.

