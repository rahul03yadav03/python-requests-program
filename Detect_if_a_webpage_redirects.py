# used to get data from a website
import requests


#take input from user
url = input("Please enter URL: ")


#add http:// if missing
if not url.startswith(("https://", "http://")):
    url = "http://" + url


try:

    #fetch the webpage
    response = requests.get(url, timeout = 10, allow_redirects=True)

    #check for error
    response.raise_for_status()

    
    # Store redirect history (empty if no redirect)
    redirect = response.history


     # If redirects exist
    if redirect:
        print("Redirected Detected !")
        print("Redirect chain: ")


        # Print each redirect step
        for r in redirect:
            print(r.status_code, "->", r.url)

        
        # Print the final URL after redirection
        print("Final URL: ", response.url)

    else:

        # No redirect happened
        print("No redirect")


#show error if any
except requests.exceptions.RequestException as e:
    print("Error", e)
        
