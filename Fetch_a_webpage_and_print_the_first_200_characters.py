# used to get data from a website
import requests


#take input from user
url = input("Please enter URL: ")


#add http:// if missing
if not url.startswith(("https://", "http://")):
    url = "http://" + url

try:


    #fetch the webpage
    response = requests.get(url, timeout=10)

    #check for error
    response.raise_for_status()

    
    #first 200 characters
    result = response.text[:200]

    
    #display result
    print("Here is your  200 text: ",result)


    
#show error if any
except requests.exceptions.RequestException as e:
    print("ERROR", e)
