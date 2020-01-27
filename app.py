import flask
from helper import *
from flask_paginate import Pagination, get_page_args, url_for

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
    usr_inp = flask.request.form['city-name'].lower()
    response = getWeatherDataLoc(usr_inp)
    city = response['city']
    if (city != ''):                                    # if user presses enter without typing
        city = city[0].upper() + city[1:]
        dateStr = getDate()
        
        return weatherdata(city)
    return flask.redirect('/')

@app.route('/weatherdata')
def weatherdata(city='Irvine'):
    # get date and weather data
    dateStr = getDate()
    response = getWeatherDataLoc(city)
    
    # pagination 
    canSearch = False
    page = int(flask.request.args.get('page', 1))
    per_page = 3
    offset = (page - 1) * per_page

    # data to be rendered
    windspeed = response['windSpeed']
    humidity = response['humidity'] * 100
    chanceRain = response['precipProbability']
    temp = str(response['temperature']) + '°'
    summary = response['summary']
    app_temp = str(response['apparentTemperature']) + '°'
    lat, long = response['latitude'], response['longitude']
    highs = [i["temperatureHigh"] for i in response["daily"]["data"]]
    lows = [i["temperatureLow"] for i in response["daily"]["data"]]
    summary = [i["summary"] for i in response["daily"]["data"]]

    # handle pages
    i = (page - 1) * per_page
    weekdays = getWeekdays()
    weekdays_for_render = weekdays[i:i+per_page]
    
    pagination = Pagination(page=page, per_page=per_page, offset=offset, total= len(weekdays), css_framework='bootstrap4', search=canSearch)


    return flask.render_template('weatherdata.html', 
                                city = city, 
                                curr_date = dateStr, 
                                weather_data = response, 
                                cards = weekdays_for_render, 
                                pagination = pagination,
                                wind = windspeed,
                                humidity = humidity,
                                chanceRain = chanceRain,
                                temp = temp,
                                condition = summary[0],
                                app_temp = app_temp,
                                lat = lat,
                                long = long,
                                curr_low = str(lows[0]) + '°',
                                curr_high = str(highs[0]) + '°',
                                high=highs, 
                                low=lows, 
                                summary=summary
                                )

@app.route('/weatherdata', methods=['POST'])
def weatherdata_post(city='Irvine'):
    usr_inp = flask.request.form['city-name'].lower()
    response = getWeatherDataLoc(usr_inp)
    city = response['city']
    if (city != ''):                                    # if user presses enter without typing
        city = city[0].upper() + city[1:]
        dateStr = getDate()
        newCityData = weatherdata(city)
        return newCityData
    return flask.redirect('/weatherdata')

if __name__ == '__main__':
    #app.debug=True
    app.run()
