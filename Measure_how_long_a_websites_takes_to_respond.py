#import requests and time library 
import requests
import time


#ask user to enter rul
url = input("Please enter URL: ")


#add http:// if missing
if not url.startswith(("https://", "http://")):
    url = "http://" + url

try:

    #set starting time
    s_time = time.time()

    #fetch the webpage
    response = requests.get(url, timeout=10)

    #check for error
    response.raise_for_status()
    
    #final time
    f_time = time.time()

    
    #we get total time after substracting final time and starting time
    t_time =  f_time - s_time

    
    #print the result
    print("Total time taken (seconds): ", t_time)

    
#show error if any
except requests.exceptions.RequestException as e:
    print("Error: ", e)
    
    
