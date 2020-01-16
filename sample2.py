import subprocess

i = 0
while i <= 10:
    subprocess.call("docker run --name tom%d -d -P tomcat"%i, shell=True)
    i = i + 1
