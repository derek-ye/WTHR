import flask
import requests
import json

app = flask.Flask(__name__)


@app.route('/')
def index():

    # no 'templates/' before file -> Flask auto checks 'templates' folder
    return flask.render_template('index.html')

@app.route('/weatherdata')
def weatherdata():

    return flask.render_template('weatherdata.html')



# API calls
def getWeatherDataLoc(loc: str): 
    """
    loc: "CITY_NAME"
    """ 
    #check for 404 errors

    # get rid of key
    gMapsKey = 'AIzaSyBAQ5Sz2UnnVnfz-57UQSJeE2gesyDdgDE'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(loc, gMapsKey)
    response = requests.get(url, verify=True)
    coords = convertLocToCoords(response)
    getWeatherDataCoords(coords)

def getWeatherDataCoords(coords: list):
    """
    data comes in form [x-coord, y-coord]
    """

    xcoord, ycoord = coords
    url = "https://api.darksky.net/forecast/afb397c644ff5187bae543cefb7eedcc/%d,%d" %(xcoord, ycoord)
    response = requests.get(url, verify=True)



# helper functions
def convertLocToCoords(response):
    """
    returns API response in [xcoord, ycoord] format
    """
    return list(json.loads(response.text)['results'][0]['geometry']['location'].values())         



if __name__ == '__main__':
    app.debug=True
    app.run()
    # getWeatherDataLoc("Irvine")