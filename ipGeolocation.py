import requests

def ip2country(ip, api_key):
    geo_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}"
    
    response = requests.get(url=geo_url)
    result = response.json()
    
    return result.get("country_name")

if __name__ == "__main__":
    user_ip = input("Enter the IP address to geolocate: ")
    api_key = "641374b665fc4280aa2d667ef00bd031"  # Hardcoded API key
    country = ip2country(user_ip, api_key)
    print(f"{user_ip} -> {country}.")

