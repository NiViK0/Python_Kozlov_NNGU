import subprocess

reply = subprocess.run(['ping', '-c', '3', '-n', '1697888.8.8.8']), 

if reply.returncode == 0:
    print('Alive')
else:
    print('Unreachable')    