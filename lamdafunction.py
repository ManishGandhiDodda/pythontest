import requests

def call_pylenin(event=None, context=None):
    r = requests.get("https://google.com")
    if r.status_code == 200:
        return "It was successful."

print(call_pylenin())

