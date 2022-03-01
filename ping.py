import subprocess

#windows ping

proc = subprocess.run(['ping', '127.0.0.1'])

print(proc.stderr)
print(proc.stdout)
print(proc.returncode)
print(proc.args)