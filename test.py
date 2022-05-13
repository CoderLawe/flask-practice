import re
from urllib import response
import requests

#DEFINE OUR BASE URL

BASE = "http://127.0.0.1:5000/"


# This makes a get request to the base URL plus hello world which was the endpoint we defined in main.py
# response = requests.get(BASE + "helloworld/lawe")

# response = requests.get(BASE + "helloworld/lawe")

data = [{"likes":10, "name":"Lawe","views":100000},
        {"likes":15, "name":"Howdy do","views":150000},
        {"likes":18, "name":"Learn contextAPI ","views":130000}

    ]

for i in range(len(data)):

    response = requests.put(BASE + "video/" + str(i), data[1])
    print(response.json())

# input()
# response = requests.delete(BASE + "video/0")
# print(response)

input()
response = requests.get(BASE + "video/2")
print(response.json())