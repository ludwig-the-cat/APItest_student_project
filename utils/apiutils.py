import requests

def getAPIData(url):
    response = requests.get(url)
    return response

