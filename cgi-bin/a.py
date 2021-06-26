#!/usr/bin/python3

print("content-type: text/html")
print()    
print("Command not Found")
import subprocess
out = subprocess.getstatusoutput("cal")
print(out[1])
