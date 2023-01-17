import requests
import json

# Make a request through the API and save it
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore data structure
response_dict = r.json()
readable_file = 'C:/PyWork/Projects/data_webapi/data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
