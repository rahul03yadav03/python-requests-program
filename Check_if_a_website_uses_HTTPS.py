# Import the requests library to send HTTP/HTTPS requests
import requests


# Ask the user to enter a website URL
url = input("Please enter a url: ")


# Remove any existing HTTP or HTTPS scheme from the input
url = url.replace("http://", "").replace("https://", "")

# Force the use of HTTPS to test if the website supports it
url = "https://" + url

try:

    # Send an HTTPS GET request to the website with a timeout
    response = requests.get(url, timeout=5)

    # If the request succeeds, the website supports HTTPS
    print("Website uses HTTPS")
        
except requests.exceptions.RequestException:

    # Handle errors such as:
    # connection error, timeout, or invalid URL
    print("Website does not use HTTPS")
