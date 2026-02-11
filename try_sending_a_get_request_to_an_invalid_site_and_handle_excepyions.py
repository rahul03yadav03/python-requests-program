#import requests library
import requests


#ask user to enter a invalid url
url = input("Please enter a url: ")


#if url do not start with "http://, https://" then add "http://"
if not url.startswith(("https://", "http://")):
    url = "http://" + url

try:

    # Send a GET request to the given URL with a timeout
    response = requests.get(url, timeout=10)

    # Raise an exception for HTTP errors 
    response.raise_for_status()

    # Print success message with HTTP status code
    print("Successful..!Status code: ", response.status_code)

except requests.exceptions.RequestException as e:

    # Handle all request-related errors such as:
    # invalid URL, connection error, timeout, or HTTP error
    print("Wrong URL or requests failed.")
    print("ERROR: ",e)
