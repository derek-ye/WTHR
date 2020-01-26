import flask
from helper import *
from flask_paginate import Pagination, get_page_args

app = flask.Flask(__name__)

@app.route('/')
def index():
    default_loc = "Irvine"

    # makes get request to the weather API
    response = getWeatherDataLoc(default_loc)

    summary = "It is " + response['summary']
    temp = str(response['temperature']) + '°'
    app_temp = response['apparentTemperature']

    date = getDate()
    return flask.render_template('index.html', temperature = temp, summary = summary, weather_data = response)

@app.route('/', methods=['POST'])
def index_post():
    city = flask.request.form['city-name'].lower()
    response = getWeatherDataLoc(city)
    if (city != ''):                                    # if user presses enter without typing
        city = city[0].upper() + city[1:]
        dateStr = getDate()
        return flask.render_template('weatherdata.html', city = city, curr_date = dateStr, weather_data = response)

    return flask.redirect('/')

@app.route('/weatherdata')
def weatherdata(city='Irvine'):
    dateStr = getDate()
    response = getWeatherDataLoc(city)

    highs = [i["temperatureHigh"] for i in response["daily"]["data"]]
    lows = [i["temperatureLow"] for i in response["daily"]["data"]]
    summary = [i["summary"] for i in response["daily"]["data"]]

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    pagination = Pagination(page=2, per_page=3, total=7, css_framework='bootstrap4')

    return flask.render_template('weatherdata.html', 
                                city = city, 
                                curr_date = dateStr, 
                                weather_data = response, 
                                cards = weekdays, 
                                pagination = pagination,
                                high=highs, 
                                low=lows, 
                                summary=summary
                                )

#prob remove
@app.route('/weatherdata', methods=['POST'])
def weatherdata_post():
    city = flask.request.form['city-name'].lower()
    city = city[0].upper() + city[1:]
    dateStr = getDate()
    return flask.render_template('weatherdata.html', city = city, curr_date = dateStr)


if __name__ == '__main__':
    app.debug=True
    app.run()
