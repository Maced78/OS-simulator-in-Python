import os

print("PID:",os.getpid())
print("PPID:",os.getppid())
print("CPU COUNT:",os.cpu_count())
import platform
print("Version and name:",platform.platform())
print("Current location:",os.getcwd())


folders = os.environ["PATH"].split(os.pathsep)

for i in folders :
	print("PATH:",i)
