#!/usr/bin/python

import subprocess
import time

proc = subprocess.Popen(["bash", "infinite_loop.sh"], close_fds=True)
print(proc.pid)
pid = proc.pid
print("Stopping in 10 seconds")
time.sleep(10)
proc = subprocess.run(['kill', '-9', str(pid)])
print(proc.returncode)
print("end")
