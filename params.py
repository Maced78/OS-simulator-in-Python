import hashlib, sys
sid = sys.argv[1]
h = hashlib.sha256(("BANM-OS-MIDTERM:" + sid).encode()).digest()
b = list(h)
b += list(hashlib.sha256(h).digest())
b += list(hashlib.sha256(h + h).digest())
b += list(hashlib.sha256(h + h + h).digest())
arr = sorted(x % 7 for x in b[3:9])
jobs = []
for i in range(6):
	burst, prio = 2 + b[9 + i] % 9, 1 + b[15 + i] % 5
	jobs.append(("P%d" % (i + 1), arr[i], burst, prio))
maxm, alloc = [], []
for i in range(5):
	row_max = [1 + b[21 + 3 * i + j] % 8 for j in range(3)]
	row_all = [b[36 + 3 * i + j] % (m + 1)
for j, m in enumerate(row_max)]
	maxm.append(row_max)
	alloc.append(row_all)
avail = [1 + b[51 + j] % 4 for j in range(3)]
k = b[54] % 5
req = [min(1 + b[55 + j] % 2, maxm[k][j] - alloc[k][j])
	for j in range(3)]
page = [1024, 2048, 4096][b[58] % 3]
start = b[59] % 16
ptable = {}
for p in range(8):
	ptable[p] = (start + 5 * p) % 16 if b[60 + p] % 3 else None
addrs = [(b[68 + 2 * i] * 256 + b[69 + 2 * i]) % (8 * page)
	for i in range(6)]
print("Student ID :", sid)
print("Sensors :", 3 + b[0] % 4)
print("Readings/sensor :", 300 + b[1] % 501)
print("Interval (ms) :", 5 + b[2] % 16)
print("Jobs (name, arrival, burst, priority):", jobs)
print("RR quantum :", 2 + b[80] % 3)
print("MLFQ quanta :", [2 + b[81] % 2, 4 + b[82] % 3, "FCFS"])
print("Frames :", 3 + b[83] % 2)
print("Reference string :", [x % 8 for x in b[84:104]])
print("Page size (bytes):", page)
print("Page table (page: frame, None = not in memory):", ptable)
print("Virtual addresses:", addrs)
print("Banker Max :", maxm)
print("Banker Allocation:", alloc)
print("Banker Available :", avail)
print("Banker request : P%d asks for %s" % (k, req))
print("Disk image :", 64 + 32 * (b[1] % 3), "blocks of",
	[512, 1024][b[2] % 2], "bytes")
print("Max files :", 16 + 8 * (b[3] % 3))
print("Log limit (KB) :", 20 + b[4] % 31)
