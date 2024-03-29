# python-scripts
Few Python scripts which might be helpful in your day-to-day life.


### 1. largest_file.py 
This script prompts the user to enter a directory path and then displays all the files in that directory in descending order of their size.
#### Necessary modules
```s
pip install os
pip install termcolor
```

### 2. public_ip.py
The script displays your public ip address.
#### Necessary modules
```s
pip install requests
```

### 3. os_Details.py
The script gathers system information and network interface details using the platform, socket, and netifaces libraries. It displays:

OS details like Python version, distribution, OS name, architecture, platform, kernel, and more.
Interface details including interface name, IPv4 address, and MAC address for each network interface, distinguishing between Windows and other systems.
###
```s
pip3 install distro netifaces
```

### 4. ipGeolocation.py
The script displays the geolocation of the provided public ip address.
#### Necessary modules
```s
pip install requests
```

### 5. ipLookUp.py
The script displays the geolocation of the provided public ip address. The script utilises a `free` API to get the geolocation.
#### Necessary modules
```s
pip install requests
```

### 6. website_ip_addr.py
This script displays the public ip address of the provided website.
#### Necessary modules
```s
pip install socket
```

### 7. add_hash.sh
This shell script will prompt you for the start and end line numbers. If you press `Enter` without entering any value, it will add `"#"` to every line. If you enter values for the start and end lines, it will add "#" only to the specified range of lines.
```s
./add_hash.sh fileName
```
