Date is 26.11.2026 --> 15:34

What I did today:

This is the first day of the project, I created a git and also added to my own github privately, in case something goes wrong,
after that I started working with the first script shown in the task, and noted down its output in README.md.

Then part A comes, I first made a prediction about how many proccesses goes on in my laptop right now, and compared it to the real result.
I counted processes , it was 2 times more than my prediction ( which was 200 but the real number was 470 ),
analyzed top 5 CPU processes, parent PIDs, shell threads, open files, and boot time.

After, created sysinfo.py and ran it from 3 places (oilfield, /tmp, and from run_sysinfo.py) 


What went wrong:

Small mistakes; wrote the code without importing os, platfrom , tried to commit to git without -m,
commited README.md while it was empty ( forgot to insert the output ).

End: about 17:28 (added on 27 Nov, I forgot to write it yesterday)



Date is 27.11.2026 --> 13:50 --> 15:30 First Session -- Second Session 19:06 --> 22:00

What I did today:

Answered to questions of Task 1, researched about process state codes, like Ss, R+ and I<. 
Then moved to Task 2, created a field.py , inside it I printed the PID and PPID's of every sensor, 
then I created a random seed, so it made the readings of the pressure reproducible, and last added a queue and logger function , and a time() parameter to meausure the total runtime.

There was a surprising thing that  about grep -c 19875 counts every line where the digits 19875 appear anywhere, not just in the PID column. One line from another sensor had those digits inside its timestamp, so grep counted 305 real lines plus 1 accidental match, giving 306. Searching for ", 19875, " only matches the PID column, so it gives exactly 305.

What went wrong:


I created the random generator in the wrong place, and printed the generator object instead of a reading.
I started the logger inside the for loop, so there were 6 loggers instead of 1. Then I called p2.start() twice.
The logger first wrote STOP lines into the file, because the else was missing.
Found that the sensors' parent was not the main process but the forkserver (Python 3.14). It was not an error, but it confused me at first.
My first ps screenshot was taken before field.py was running, so it did not show the sensors.


Date is 28.11.2026 --> 13:23 --> 

What I did today:

What went wrong: