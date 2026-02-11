# Import the requests library to send HTTP requests
import requests


# Ask the user how many URLs they want to check
number = int(input("Enter how many url do you want to check: "))

# Create a list to store all the URLs
urls = []

# Take URL input from the user and add to the list
for n in range(number):
    url = input(f"Please enter your {n+1} url: ")
    urls.append(url)


# Loop through each URL in the list to check reachability
for url in urls:


    # If the URL does not start with 'http://' or 'https://', add 'http://'
    if not url.startswith(("https://", "http://")):
        url = "http://" + url

    try:

        # Send a GET request to the URL with a timeout of 5 seconds
        response = requests.get(url, timeout = 5)


        # Raise an exception for HTTP error responses
        response.raise_for_status()


        # If request succeeds, print that the URL is reachable
        print(f"Reachable: {url}")


    except requests.exceptions.RequestException:

        # If any request-related error occurs, print that the URL is not reachable
        print(f"Not reachable: {url}")
