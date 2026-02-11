# Import the requests library to send HTTP requests
import requests

# Ask the user to enter a URL and remove any leading/trailing spaces
url = input("PLease enter a URL: ").strip()


# If the user did not include the HTTP or HTTPS scheme, add "http://"
if not url.startswith(("http://", "https://")):
    url = "http://" +url

try:

    # Send a GET request to the URL with a timeout of 10 seconds
    response = requests.get(url, timeout=10)
    
    # Raise an exception if the HTTP request returned an error status
    response.raise_for_status()

    # Access the HTTP headers returned by the server
    header = response.headers

    # Print a message indicating that the headers will be displayed
    print("HERE is a header of webpage: ")


    # Print each header (key: value) from the server's response
    for key, value in header.items():
        print(f"{key} : {value}")


except requests.exceptions.RequestException as e:

    # Catch any request-related errors such as connection issues, invalid URLs, timeouts, or HTTP errors
    print("Error..! ", e)
