import requests
import json
import datetime
from config import gmaps_api_key, dark_sky_api_key

# API calls
def getWeatherDataLoc(loc: str): 
    """
    loc: "CITY_NAME"
    """ 
    #check for 404 errors

    # get rid of key
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(loc, gmaps_api_key)
    response = requests.get(url, verify=True)
    coords = convertLocToCoords(response)
    getWeatherDataCoords(coords)

def getWeatherDataCoords(coords: list):
    """
    data comes in form [x-coord, y-coord]
    """

    xcoord, ycoord = coords
    url = "https://api.darksky.net/forecast/%s/%f,%f" %(dark_sky_api_key, xcoord, ycoord)
    print(url)
    response = json.loads(requests.get(url, verify=True).text)
    return getUsefulData(response)

# helper functions
def convertLocToCoords(response):
    """
    returns API response in [xcoord, ycoord] format
    """
    return list(json.loads(response.text)['results'][0]['geometry']['location'].values())         


def getUsefulData(response):
    info = {}
    info['latitude'] = response['latitude']
    info['longitude'] = response['longitude']
    info['summary'] = response['currently']['summary']
    info['icon'] = response['currently']['icon']
    info['humidity'] = response['currently']['humidity']
    info['precipProbability'] = response['currently']['precipProbability']
    info['apparentTemperature'] = response['currently']['apparentTemperature']
    info['windSpeed'] = response['currently']['windSpeed']
    info['daily'] = response['daily']
    print(info)
    return info

def getDate():
    today = datetime.date.today()
    dateStr = today.strftime("%A, %B %d")
    return dateStr
