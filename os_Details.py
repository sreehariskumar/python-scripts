import platform
import socket
import netifaces
import distro

def get_distro_info():
    try:
        dist = distro.linux_distribution(full_distribution_name=False)
        return " ".join(dist).strip()
    except:
        return "N/A"

def get_interface_details():
    interface_details = []
    interfaces = netifaces.interfaces()
    
    for iface in interfaces:
        if iface != 'lo':
            addrs = netifaces.ifaddresses(iface)
            ipv4_addr = addrs.get(netifaces.AF_INET, [{'addr': 'N/A'}])[0]['addr']
            mac_addr = addrs.get(netifaces.AF_LINK, [{'addr': 'N/A'}])[0]['addr']
            interface_details.append((iface, ipv4_addr, mac_addr))
    
    return interface_details

def get_windows_interface_details():
    interface_details = []
    for iface, addrs in netifaces.gateways().items():
        ipv4_addr = addrs.get(netifaces.AF_INET, [])[0]
        mac_addr = netifaces.ifaddresses(iface).get(netifaces.AF_LINK, [{'addr': 'N/A'}])[0]['addr']
        interface_details.append((iface, ipv4_addr, mac_addr))
    
    return interface_details

print("----------OS DETAILS----------")
print("Python version:", platform.python_version())
print("Distribution:", get_distro_info())
print("Operating System:", platform.system())
print("Architecture:", platform.machine())
print("Platform:", platform.platform())
print("Kernel:", platform.release())
print("------------------------------")

print("------INTERFACE DETAILS------")
if platform.system() == 'Windows':
    interface_details = get_windows_interface_details()
else:
    interface_details = get_interface_details()

for iface, ipv4_addr, mac_addr in interface_details:
    print("Interface:", iface)
    print("IPv4 Addr:", ipv4_addr)
    print("HW MAC Addr:", mac_addr)
    print("------------------------------")
