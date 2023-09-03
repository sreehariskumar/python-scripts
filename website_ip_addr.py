import socket
host_name = input("Enter the website address: ")
print(f'The {host_name} IP address is: {socket.gethostbyname(host_name)}')
