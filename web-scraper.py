#Python Web Sraber by KxroShinigami

#ToDo: pysimplegui, time countdown
# https://realpython.com/pysimplegui-python/
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/, https://realpython.com/python-sleep/

# +--+--+--+--+--+--+
#    Imports

import requests
from bs4 import BeautifulSoup


# +--+--+--+--+--+--+
#    Input

print("Please enter a valid Website URL:")
print("Example: 'https://www.google.com'")
Website = input()

#TEST
Website = "https://www.mediamarkt.de/de/campaign/angebote-computer-buero#root"


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
elif(StatusCode == "403"):
    Status = "Forbidden"
elif(StatusCode == "404"):
    Status = "Not Found"
elif(StatusCode == "410"):
    Status = "Gone"
elif(StatusCode == "500" or StatusCode == "503"):
    Status = "Unavailable"
else:
    Status = "Weird"

print("Your Website is:", Status, "(", StatusCode, ")\n\n")


# +--+--+--+--+--+--+
#    Parsing the HTML

soup = BeautifulSoup(WebsiteGetRequest.content, 'html.parser')


# +--+--+--+--+--+--+
#    Display some information

print(soup.title)


# +--+--+--+--+--+--+
#    Extraction of Content

print("\n\nYour Content is: \n\n")

s = soup.find('p', class_='BaseTypo-sc-1jga2g7-0 izkVco StyledInfoTypo-sc-1jga2g7-1 doYUxh')

lines = s
 
for line in lines:
    print(line.text)


# Informationen MediaMarkt Produkt-Namen
# class="BaseTypo-sc-1jga2g7-0 izkVco StyledInfoTypo-sc-1jga2g7-1 doYUxh"

# Informationen MediaMarkt Preise
# class="StyledUnbrandedPriceDisplayWrapper-sc-1n9i68m-0 gWEOl"
    # "ScreenreaderTextSpan-sc-11hj9ix-0 kZCfsu"





# +--+--+--+--+--+--+
#    Searching for relevant Information