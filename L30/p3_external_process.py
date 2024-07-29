import os
from time import sleep

# code = os.system("git --version")
# print(f"code={code}")

# os.popen()

import subprocess

# command = "ls -la"
# result = subprocess.run(command.split())
# print(result)
# print(result.returncode)

# command = "sleep 3"
# result = subprocess.run(command.split())
# print("AFTER")


# command = "ls -la"
# result = subprocess.run(command.split(), capture_output=True, text=True)
# print(result)
# print(result.returncode)
# print(result.stdout)
# #print(result.stdout.decode())


# command = "python3 input_example.py"
# result = subprocess.run(command.split(), capture_output=True, input=b'5')
# print(result)
# print(result.returncode)
# print(result.stdout)
# print(result.stdout.decode())


# command = "python3 input_example.py"
# result = subprocess.run(command.split(), capture_output=True, input='5', text=True)
# print(result)
# print(result.returncode)
# print(result.stdout)

# command = "ls -la qqqq"
# result = subprocess.run(command.split(), capture_output=True)
# print(result)
# print(result.stdout)
# print(result.stderr)
# print(result.returncode)


# command = "ls -la qqqq"
# result = subprocess.run(command.split(), stderr=subprocess.DEVNULL)
# print(result)
# print(result.stdout)
# print(result.stderr)
# print(result.returncode)

# command = "bash script.sh"
# result = subprocess.run(command.split())
# print(result)
# print(result.stdout)
# print("AFTER")

# command = "bash script.sh"
# process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# print(process)
# stdout, stderr = process.communicate(timeout=10)
# for i in range(5):
#     print(f"Main {i}")
#     sleep(0.1)
#
# print("AFTER")
# print(stdout)


# file = 'output.log'
# command = "bash script.sh"
# process = subprocess.Popen(command.split(), stdout=open(file, 'w'))
# print(process)
# stdout, stderr = process.communicate(timeout=10)
# for i in range(5):
#     print(f"Main {i}")
#     sleep(0.1)
#
# print("AFTER")
# print(stdout)


file = 'output.log'
command = "bash script.sh"
process = subprocess.Popen(command.split())

while process.poll() is None:
    sleep(1)
print(process.poll())


print("AFTER")

