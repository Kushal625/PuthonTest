import requests
import json 

response = requests.get("http://jsonplaceholder.typicode.com/todos")

tasks = json.loads(response.text)


for entry in tasks:
    if entry["completed"] == True:
        print(entry["userId"],entry["title"] )


