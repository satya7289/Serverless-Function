import sys
import requests

# main() will be invoked when you invoke this action.
#
# When enabled as a web action, use the following URL to invoke this action:
# https://{APIHOST}/api/v1/web/{QUALIFIED ACTION NAME}?location=Austin
#
# For example:
# https://openwhisk.ng.bluemix.net/api/v1/web/myusername@us.ibm.com_myspace/get-http-resource/location?location=Austin
#
# In this case, the params variable will look like:
# { "location": "Austin" }
"""
API for getting a random joke :  http://api.icndb.com/jokes/random
"""


# Available Types: "top-headlines", "sources", "everything"
def main(param):
    
    url = "http://api.icndb.com/jokes/random"
        
    headers = {'accept': 'application/json'}
    Joke = requests.get(url)
    # print Joke
    if Joke.status_code != 200:
        return {
        'statusCode': Joke.status_code,
        'headers': { 'Content-Type': 'application/json'},
        'body': {'message': 'Error processing your request'}
    }
    else:
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json'},
            'body': {'joke': Joke.json()['value']['joke'], 'categories': Joke.json()['value']['categories']}
        }

print(main({'name':'satya'}))
