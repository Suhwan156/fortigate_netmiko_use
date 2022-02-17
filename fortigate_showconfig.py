from getpass import getpass

from netmiko import ConnectHandler

password = getpass()

device_ip = ["10.10.10.10", "10.10.10.11"]

# A list comprehension
devices = [
    {
        "device_type": "fortinet",
        "host": ip,
        "username": "admin",
        "password": password,
    }
    for ip in device_ip
]

for device in devices:
    print(f'Connecting to the device: {device["host"]}')

    with ConnectHandler(**device) as net_connect:  # Using Context Manager
        show_full = net_connect.send_command(
            "show full-configuration"
        )  # Inside the connection

    print(show_full)