import requests

resp = requests.post("https://textbelt.com/text", {
    "phone" : 3109759608,
    "message" : "Good Evening Yanick take2",
    "key" : "textbelt"
})
print(resp.json())