import requests
import json
import datetime
from config import gmaps_api_key, dark_sky_api_key

# API calls
def getWeatherDataLoc(city: str): 
    #check for 404 errors

    # get rid of key
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(city, gmaps_api_key)
    response = requests.get(url, verify=True)
    coords = convertLocToCoords(response)
    return getWeatherDataCoords(city, coords)

def getWeatherDataCoords(city: str, coords: list):
    """
    data comes in form [x-coord, y-coord]
    """

    xcoord, ycoord = coords
    url = "https://api.darksky.net/forecast/%s/%f,%f" %(dark_sky_api_key, xcoord, ycoord)
    response = json.loads(requests.get(url, verify=True).text)
    # print(response)
    return getUsefulData(city, response)

# helper functions
def convertLocToCoords(response):
    """
    returns API response in [xcoord, ycoord] format
    """
    return list(json.loads(response.text)['results'][0]['geometry']['location'].values())         


def getUsefulData(city: str, response):
    info = {}
    info["city"] = city
    info['temperature'] = response['currently']['temperature']
    info['apparentTemperature'] = response['currently']['apparentTemperature']
    info['latitude'] = response['latitude']
    info['longitude'] = response['longitude']
    info['summary'] = response['currently']['summary']
    info['icon'] = response['currently']['icon']
    info['humidity'] = response['currently']['humidity']
    info['precipProbability'] = response['currently']['precipProbability']
    info['apparentTemperature'] = response['currently']['apparentTemperature']
    info['windSpeed'] = response['currently']['windSpeed']
    info['hourly'] = response['hourly']
    info['daily'] = response['daily']
    # print(info)
    return info

def getDate():
    today = datetime.date.today()
    #dateStr = today.strftime("%A, %B %d")

    #returns day of the week
    dateStr = today.strftime("%A")
    return dateStr

def getWeekdays():
    '''
    Creates an array for the daily weather view, starting from the current day
    '''
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    date = getDate()
    todaysIndice = weekdays.index(date)
    
    return weekdays[todaysIndice:] + weekdays[:todaysIndice]