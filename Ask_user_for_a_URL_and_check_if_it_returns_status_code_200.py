#import socket library
import requests


# Ask the user for a URL
url = input("Please Enter a Url: ").strip()


# If the URL does not start with http:// or https://, add http:// by default
if not url.startswith(("https://", "http://")):
    url = "http://" + url


try:

    # Send a GET request
    response = requests.get(url)

    code = response.status_code


    # Check the status code
    if code == 200:
        print(f"Success! The URL {url} return status code 200.")


    else:
        print(f"The URL {url} returned status code {code}")



except requests.exceptions.RequestException as e:
    print(f"Error accessing the URL: {e}")
