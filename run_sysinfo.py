import subprocess, os
print("run_sysinfo PID:", os.getpid())
subprocess.run(["python3", "sysinfo.py"])
