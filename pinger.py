import os

ip = ['127.0.0.1', '8.0.0.1', '192.168.0.10', '192.168.10.10']

for ip_addresses in ip:
    print(ip_addresses)

ping = f"ping -c 1 -W 2 {ip} > ./dev 2>&1"

exit_code = os.system(ping)

print(exit_code)