import flask
from helper import *

app = flask.Flask(__name__)

@app.route('/')
def index():
    default_loc = "Irvine"

    # makes get request to the weather API
    x = getWeatherDataLoc(default_loc)

    summary = "It is " + x['summary']
    temp = str(x['temperature']) + '°'
    app_temp = x['apparentTemperature']

    date = getDate()
    return flask.render_template('index.html', temperature = temp, summary = summary)

@app.route('/', methods=['POST'])
def index_post():
    city = flask.request.form['city-name'].lower()
    print(city)
    if (city != ''):                                    # if user presses enter without typing
        city = city[0].upper() + city[1:]
        dateStr = getDate()
        return flask.render_template('weatherdata.html', city = city, curr_date = dateStr)
    return flask.redirect('/')

@app.route('/weatherdata')
def weatherdata(city='Irvine'):
    dateStr = getDate()
    return flask.render_template('weatherdata.html', city = city, curr_date = dateStr)

@app.route('/weatherdata', methods=['POST'])
def weatherdata_post():
    city = flask.request.form['city-name'].lower()
    city = city[0].upper() + city[1:]
    dateStr = getDate()
    return flask.render_template('weatherdata.html', city = city, curr_date = dateStr)


if __name__ == '__main__':
    app.debug=True
    app.run()
    # getWeatherDataLoc("Irvine")
    # getDate()