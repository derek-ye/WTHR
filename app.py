import flask
import requests

app = flask.Flask(__name__)


@app.route('/')
def index():

    # no 'templates/' before file -> Flask auto checks 'templates' folder
    return flask.render_template('index.html')

@app.route('/weatherdata')
def weatherdata():

    return flask.render_template('weatherdata.html')



# API calls
def getWeatherData(coords: list):  # data comes in form [x-coord, y-coord]
    xcoord, ycoord = coords
    response = requests.get("https://api.darksky.net/forecast/afb397c644ff5187bae543cefb7eedcc/%d,%d" %(xcoord, ycoord))


if __name__ == '__main__':
    app.debug=True
    app.run()