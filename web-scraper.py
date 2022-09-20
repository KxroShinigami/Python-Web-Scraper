#Python Web Sraber by KxroShinigami

#ToDo: pysimplegui, time countdown
# https://realpython.com/pysimplegui-python/
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/, https://realpython.com/python-sleep/

# +--+--+--+--+--+--+
#    Imports

import requests


# +--+--+--+--+--+--+
#    Input

print("Please enter a valid Website URL:")
print("Example: 'https://www.google.com'")
Website = input()

# +--+--+--+--+--+--+
#    Get-Request Website

WebsiteGetRequest = requests.get(Website)


# +--+--+--+--+--+--+
#    Status Code Website

# 1xxs – Informational responses
# 2xxs – Success
# 3xxs – Redirection
# 4xxs – Client errors: Page not found.
# 5xxs – Server errors: Failure.

StatusCode = str(WebsiteGetRequest.status_code)

if(StatusCode == "200"):
    Status =  "Online"
elif(StatusCode == "404"):
    Status = "Not Found"

print("Your Website is:", Status)