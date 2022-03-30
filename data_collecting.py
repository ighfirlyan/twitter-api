import requests
import json

# response =  requests.get("https://masak-apa.tomorisakura.vercel.app/api/recipes")
# print(response.status_code)
# print(response.text)

parameters = {
    'q':'coto'
}

response = requests.get("https://masak-apa.tomorisakura.vercel.app/api/recipes", params=parameters)
print(response.status_code)
# print(response.text)

text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)