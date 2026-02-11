#import requests library
import requests


#ask user to enter url
url = input("please enter URL: ")


#add http:// if missing
if not url.startswith(("https://", "http://")):
    url = "http://" + url


try:

    #fetch the webpage
    response = requests.get(url, timeout=10)

    #check for error
    response.raise_for_status()

    #store all charcter in "text"
    text = response.text

    
    #open one file and put "text" into this file
    with open("file.txt", "w", encoding = "utf-8") as f:
        result = f.write(text)


    #print this to confirm it
    print("website HTML successfully saved to file.txt")


#show error if any
except requests.exceptions.RequestException as e:
    print("ERROR !: ", e)
