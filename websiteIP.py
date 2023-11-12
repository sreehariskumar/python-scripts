#import socket

#def print_colored(text, color):
#    colors = {
#        'green': '\033[92m',
#        'red': '\033[91m',
#        'reset': '\033[0m'
#    }
#    return f'{colors[color]}{text}{colors["reset"]}'

#host_name = input("Enter the website address: ")
#ip_address = socket.gethostbyname(host_name)

#formatted_output = f'IP address of {print_colored(host_name, "green")}: {print_colored(ip_address, "red")}'
#print(formatted_output)

import sys
import socket

def print_colored(text, color):
    colors = {
        'green': '\033[92m',
        'red': '\033[91m',
        'reset': '\033[0m'
    }
    return f'{colors[color]}{text}{colors["reset"]}'

def get_ip_address(host_name):
    try:
        ip_address = socket.gethostbyname(host_name)
        return f'IP address of {print_colored(host_name, "green")}: {print_colored(ip_address, "red")}'
    except socket.gaierror:
        return f'Unable to resolve the IP address for {print_colored(host_name, "green")}'

if len(sys.argv) != 2:
    print("Usage: python website_ip_addr.py <website_name>")
    sys.exit(1)

website_name = sys.argv[1]
output = get_ip_address(website_name)
print(output)

