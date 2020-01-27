import requests
import json
import datetime
from config import gmaps_api_key, dark_sky_api_key

# API calls
def getWeatherDataLoc(city: str): 

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(city, gmaps_api_key)
    response = json.loads(requests.get(url, verify=True).text)
    foundCity = response['results'][0]['formatted_address']
    coords = convertLocToCoords(response)
    return getWeatherDataCoords(foundCity, coords)

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
    returns API response (as a JSON) in [xcoord, ycoord] format
    """
    return list(response['results'][0]['geometry']['location'].values())         


def getUsefulData(city: str, response):
    """
    return a dictionary with the selected information, as well as hourly and daily info

    """
    info = {}
    info["city"] = city
    info['temperature'] = response['currently']['temperature']
    info['apparentTemperature'] = response['currently']['apparentTemperature']
    info['latitude'] = "%.2f" % response['latitude']
    info['longitude'] = "%.2f" % response['longitude']
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
    """
    Creates an array for the daily weather view, starting from the current day
    """
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    date = getDate()
    todaysIndice = weekdays.index(date)
    
    return weekdays[todaysIndice:] + weekdays[:todaysIndice]