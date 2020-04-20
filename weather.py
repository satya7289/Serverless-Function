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
API for getting weather:  https://openweathermap.org/
ApiKey = "55f7cd557c42082a63dd21a10218e859"
"""


# Available Types: "top-headlines", "sources", "everything"
def main(param):

    Lat = param['latitude'] if 'latitude' in param else ""
    Lng = param['longitude'] if 'longitude' in param else ""
    City = param['city'] if 'city' in param else ""
    # setting ApiKey from https://newsapi.org/
    ApiKey = "55f7cd557c42082a63dd21a10218e859"
    Url = "api.openweathermap.org/data/2.5/"
    if City!="":
        Weather_Url = Url + "weather?q=" + City + "&appid=" + ApiKey
    if Lng!="" and Lat!="":
        Weather_Url = Url + "weather?lat=" + Lat + "&lon=" +Lng + "&appid=" + ApiKey
    
    headers = {'accept': 'application/json'}
    Weather = requests.get(Url,Weather_Url)
    print(Weather)
    if Weather.status_code != 200:
        return {
        'statusCode': Weather.status_code,
        'headers': { 'Content-Type': 'application/json'},
        'body': {'message': 'Error processing your request'}
    }
    else:
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json'},
            'body': Weather.json()
        }

print(main({'city':'jodhpur'}))
