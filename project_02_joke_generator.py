import requests

# Official Joke API endpoint
url = "https://official-joke-api.appspot.com/random_joke"

# Send request to fetch a random joke
response = requests.get(url)

# Check if joke was retrieved successfully
if response.status_code == 200:
    joke = response.json()
    print("\n--- Here is a Joke for You! ---")
    print("Setup:", joke["setup"])
    print("Punchline:", joke["punchline"])
else:
    print("Failed to fetch a joke. Please check your internet connection.")
