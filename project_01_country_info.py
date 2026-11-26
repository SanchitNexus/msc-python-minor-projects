import requests

# Ask user for country name
country = input("Enter country name: ")

# Free Country API endpoint
url = "https://countriesnow.space/api/v0.1/countries/capital"

# Send request to fetch country details
response = requests.get(url)

# Check if data was retrieved successfully
if response.status_code == 200:
    countries = response.json()["data"]
    found = False
    for item in countries:
        if item["name"].lower() == country.lower():
            print("\n--- Country Information ---")
            print("Name:", item["name"])
            print("Capital:", item["capital"])
            print("ISO Code:", item["iso2"])
            found = True
            break
    if not found:
        print("Country not found. Please check the spelling.")
else:
    print("API is currently unavailable.")
