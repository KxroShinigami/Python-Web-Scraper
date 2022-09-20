#Python Web Sraber by KxroShinigami

#ToDo: pysimplegui, time countdown



import requests

# Making a GET request
r = requests.get('www.google.com')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)