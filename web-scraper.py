#Python Web Sraber by KxroShinigami

#ToDo: pysimplegui, time countdown
# https://realpython.com/pysimplegui-python/
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/, https://realpython.com/python-sleep/

# +--+--+--+--+--+--+
#    Imports

import io
import requests
from bs4 import BeautifulSoup
import pyfiglet
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageTk
from urllib.request import urlopen, Request
import json

# +--+--+--+--+--+--+
#    Banner

#ascii_banner = pyfiglet.figlet_format("Python Web Scraber")
#print(ascii_banner)


# +--+--+--+--+--+--+
#    Websites

WebsiteMediaMarkt_Angebote_ComputerBüro = "https://www.mediamarkt.de/de/campaign/angebote-computer-buero#root"
WebsiteMediaMarkt_Angebote_GamingVR = "https://www.mediamarkt.de/de/campaign/angebote-gaming-vr#root"
WebsiteAmazon_SpeedDeals = "https://www.amazon.de/s?k=grafikkarten&i=computers"
                            
# +--+--+--+--+--+--+
#    Basic Functions

def PrintWebsite(GivenWebsite):
    print("The current Website is:", GivenWebsite)

def Scrape():
    #takes Website selected with RadioButton and calls function
    if(RBtext_var.get() == RBtexts[0]):
        x = MediaMarkt(WebsiteMediaMarkt_Angebote_ComputerBüro)
        print(x)
    elif(RBtext_var.get() == RBtexts[1]):
        x = MediaMarkt(WebsiteMediaMarkt_Angebote_GamingVR)
        print(x)
    elif(RBtext_var.get() == RBtexts[2]):
        x = Amazon(WebsiteAmazon_SpeedDeals)
        print(x)
    else:
        print("WTF")


# /\/\/\/\/\/\/\/\/\/\/\
#    MediaMarkt Website Begin
# /\/\/\/\/\/\/\/\/\/\/\
def MediaMarkt(Website):
    
    PrintWebsite(Website)

    print("Watch Out: The current prices are the basic prices, no specific extra sale (work in progress)")

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

    print("#\n\nThe Website is:", Status, "(", StatusCode, ")\n")


    # +--+--+--+--+--+--+
    #    Parsing the HTML

    soup = BeautifulSoup(WebsiteGetRequest.content, 'html.parser')


    # +--+--+--+--+--+--+
    #    Display some information

    #print("#\n\n", soup.title, "\n")


    # +--+--+--+--+--+--+
    #    Extraction of Content

    product_name = []
    product_price = []
    product_ratings = []
    product_links = []


    for a in soup.findAll('div', attrs={'class':'StyledCell-sc-1wk5bje-0 fosUOY StyledProductCell-mws94n-2 jptNHu'}):
        name = a.find('p', attrs={'class':'BaseTypo-sc-1jga2g7-0 izkVco StyledInfoTypo-sc-1jga2g7-1 doYUxh'})
        price = a.find('span', attrs={'class':'ScreenreaderTextSpan-sc-11hj9ix-0 kZCfsu', 'aria-hidden':None})

        rating = str(a.find('div', attrs={'class':'StyledRatingWrapper-sc-15s0par-0 gIJkAn StyledRating-q99jve-1'}))
        ratingstarscount = rating.count("mms-fully-rated-star")

        links = a.find('a', attrs={'class':'StyledLinkRouter-sc-1drhx1h-2 dcWIdZ StyledProductLink-mws94n-5 NxdrW', 'href':True})
        
        if(type(name) == None or type(price) == None):
            print("Something went wrong (Couldnt find a object)")
            break

        product_name.append(name.text)
        product_price.append(price.text)
        product_ratings.append(ratingstarscount)
        product_links.append(links.get('href'))


    # +--+--+--+--+--+--+
    #    Marking special information




    # +--+--+--+--+--+--+
    #    Output of relevant Information

    product_list = {}

    for b in range(len(product_name)):
        product_list.update({
            "Product " + str(b) : {
                "name" : product_name[b],
                "price" : product_price[b],
                "rating" : product_ratings[b],
                "link" : "www.mediamarkt.de" + product_links[b]
                }
            })

    result = json.dumps(product_list, 
                        indent = 6,
                        separators =("", " = "))
    
    return result

# /\/\/\/\/\/\/\/\/\/\/\
#    MediaMarkt Website End
# /\/\/\/\/\/\/\/\/\/\/\

# +--+--+--+--+--+--+
#    GUI

#tk._test()

# +-+ General +-+

root = tk.Tk()
root.title("Python Web Scraber")

pane = Frame(root)
pane.pack(fill = BOTH, expand = True)

root.resizable(False, False) # Height and Width unresizable
root.attributes('-topmost', 1) # Window always on top

# +-+ Radiobutton Text +-+

RBtext_var = tk.StringVar()
RBtexts = ('MediaMarkt -> Angebote -> Computer & Büro',
            'MediaMarkt -> Angebote -> Gaming & VR',
            'Amazon -> Speed Deals')

# +-+ LabelFrame "Choose Website" with Radiobuttons +-+

# Frame
lf_ChooseWebsite = ttk.LabelFrame(root, text='Choose Website')
lf_ChooseWebsite.pack( fill = BOTH, expand = True)

#Radiobuttons

for RBtext in RBtexts:
    # create a radio button
    radio = ttk.Radiobutton(lf_ChooseWebsite, text=RBtext, value=RBtext, variable=RBtext_var)
    radio.pack(side = TOP, fill = BOTH, expand = False)

# +-+ Button "Scrape" +-+

scrape_button = ttk.Button(
    root,
    text = "Scrape",
    command = Scrape
)

scrape_button.pack(side = TOP, fill = BOTH, expand = False)

# +-+ LabelFrame Alarms +-+

# Frame
lf_ChooseWebsite = ttk.LabelFrame(root, text='Alarms')
lf_ChooseWebsite.pack( fill = BOTH, expand = True)

# +-+ Photos +-+

url = "https://stickerobot.com/wp-content/uploads/2013/05/nyan-cat-sticker.jpg"

request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

my_page = urlopen(request)

my_picture = io.BytesIO(my_page.read())

pil_img = Image.open(my_picture)

tk_img = ImageTk.PhotoImage(pil_img)

label = tk.Label(root, image=tk_img, width = 300, height = 200)
label.pack(side = TOP, padx = 5, pady = 5)

# +-+ Button "Exit" +-+

exit_button = ttk.Button(
    root,
    text = "Exit",
    command = lambda: root.quit()
)

exit_button.pack(side = BOTTOM, fill = BOTH, expand = False)

# +-+ Mainloop +-+

root.mainloop()