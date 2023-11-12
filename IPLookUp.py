import sys
import requests

def get_ip_info(ip_address):
    api_url = f"https://ipinfo.io/{ip_address}/geo"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    # Check if an IP address is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 IPLookUp.py <IP_address>")
        sys.exit(1)

    # Get the IP address from the command-line argument
    ip_address = sys.argv[1]

    # Get IP information using the API
    ip_info = get_ip_info(ip_address)

    # Print the output
    if ip_info:
        print("\nIP Information:")
        print(f"IP Address: {ip_info['ip']}")
        print(f"City: {ip_info['city']}")
        print(f"Region: {ip_info['region']}")
        print(f"Country: {ip_info['country']}")
        print(f"Location: {ip_info['loc']}")
        print(f"Organization: {ip_info['org']}")
        print(f"Postal Code: {ip_info['postal']}")
        print(f"Timezone: {ip_info['timezone']}")
        print(f"Readme: {ip_info['readme']}")
    else:
        print(f"Failed to retrieve information for IP address: {ip_address}")

if __name__ == "__main__":
    main()
