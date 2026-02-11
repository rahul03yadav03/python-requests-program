#import requests library
import requests

#ask user to enter api url
api = input("Please enter API url: ")


#add http:// if missing
if not api.startswith(("https://", "http://")):
    api = "http://" + api

try:


    #fetch the webpage
    response = requests.get(api, timeout=10)

    #check for error
    response.raise_for_status()

    # Convert the response to JSON format (Python dictionary)
    data = response.json()


    # Print the JSON response
    print("JSON Response: ",data)


# Handle network-related errors (e.g., connection issues, timeout)
except requests.exceptions.RequestException as e:
    print("Error: ", e)


# Handle cases where the response is not valid JSON
except ValueError:
    print("error: Response is not valid JSON")
