import sys
import requests

"""
API for getting latest news from newsapi:  https://newsapi.org/account
"""

# Available Types: "top-headlines", "sources", "everything"
def main(param):
    Type = param['type'] if 'type' in param else "top-headlines"
    Country = param['country'] if 'country' in param else "us"
    Query = param['query'] if 'query' in param else ""
    # setting ApiKey from https://newsapi.org/
    ApiKey = "3ea2264ad3854825936b1b437b22a34b"
    Url = "http://newsapi.org/v2/"
    if Query=="":
        News_Url = Url + Type + "?country=" + Country + "&apiKey=" + ApiKey
    else:
        News_Url = Url + "?q=" + Query + "&apiKey=" + ApiKey

    headers = {'accept': 'application/json'}

    News = requests.get(News_Url)

    if News.status_code != 200:
        return {
        'statusCode': News.status_code,
        'headers': { 'Content-Type': 'application/json'},
        'body': {'message': 'Error processing your request'}
    }
    else:
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json'},
            'body': News.json()
        }

print(main({'type':'top-headlines','country':'us'}))