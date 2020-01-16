import subprocess
subprocess.call("docker pull registry", shell=True);

print("****** containers ******")
subprocess.call("docker container ls", shell=True)


