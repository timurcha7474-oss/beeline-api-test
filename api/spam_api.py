import requests

def send_spam(data):
    url = "https://moskva.beeline.ru/api/spam-feedback"

    response = requests.post(url, json = data)
    return response