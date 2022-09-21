# import the os system
import os

# create a variable and give it the value of a list
ip = ['127.0.0.1', '8.0.0.1', '192.168.0.10', '192.168.10.10']

# create a for loop
for ip_addresses in ip:
    print(ip_addresses)

# create a variable where it pings the IP addresses in the list
ping = f"ping -c 1 -W 2 {ip} > ./dev 2>&1"

# create a variable where it shows if the ping went through
exit_code = os.system(ping)

# print the variable to show if the ping went through
print(exit_code)