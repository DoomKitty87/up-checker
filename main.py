import platform
import subprocess
import time
def ping_host(host):
  command = ["ping", "-n" if platform.system().lower() == "windows" else "-c", "1", host]
  return subprocess.call(command) == 0

if (__name__ == "__main__"):
  while(True):
    with open("hosts.list", "r") as hosts_file:
      hosts = hosts_file.read().splitlines()
      for host in hosts:
        if (ping_host(host)):
          print(host + " is up")
        else:
          print(host + " is down")
    time.sleep(60)
    