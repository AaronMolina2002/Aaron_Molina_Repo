import os

ip = "127.0.0.1"

ping_cmd = f"ping -c 1 -W 2 {ip} > ./dev 2>&1"

exit_code = os.system(ping_cmd)

print(exit_code)