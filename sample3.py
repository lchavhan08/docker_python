import subprocess

i = 0
while i<= 10:
    subprocess.call("docker rm -f tom%d"%i, shell=True)
    i = i + 1
