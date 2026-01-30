# import urllib.request

# # contents = urllib.request.urlopen("http://melanzana.com/products/2025-micro-grid-hoodie-v2?store=online").read()

# url = "http://melanzana.com/products/2025-micro-grid-hoodie-v2?store=online"
# req = urllib.request.urlopen(url, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
# gcontext = ssl.SSLContext()  # Only for gangstars
# info = urllib2.urlopen(req, context=gcontext).read()


# print(contents)

import urllib.request
import ssl # Required for HTTPS context
import certifi
from threading import Timer
import datetime
import sys
from playsound import playsound
import webbrowser


check_interval = 20
url = "http://melanzana.com/products/2025-micro-grid-hoodie-v2?store=online"


def checkSiteForRestockMessage():
   # Create a default SSL context for handling HTTPS certificates
   # context = ssl.create_default_context()
   context = ssl.create_default_context(cafile=certifi.where())

   try:
       # Open the URL with the secure context
       with urllib.request.urlopen(url, context=context) as response:
           # Read and decode the response
           html_content = response.read().decode('utf-8')
           # print("Request successful!")
           # print(html_content)

           return "Monday, January 26th, between noon and 3pm" in html_content

   except urllib.error.URLError as e:
       print(f"An error occurred: {e.reason}")
       return False


def infinite_alert():
   webbrowser.open(url)
   while True:
      print("GO GO GO")
      playsound("alert-109578.mp3")


def looper():
   restock_message_present = checkSiteForRestockMessage()
   print (datetime.datetime.now(), "same" if restock_message_present else "CHANGED")

   if not restock_message_present:
      infinite_alert()
      return

   Timer(check_interval, looper).start()



try:
   looper()
except Exception as e:
   print(e)
   print("ERROR")
   while True:
      playsound("alert-109578.mp3")