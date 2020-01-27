# WTHR

WTHR is a Flask webapp that reports daily and weather data.\
#### Check it out at [wthr.derekye.com](wthr.derekye.com)!
  
---

## Installation

After cloning, cd into the project directory and enter

```bash
python3 app.py
```

to run app in the development mode.\
Open http://127.0.0.1:5000/ to view it in the browser.


## Running the tests

* Requirements (more info [here](https://nightwatchjs.org/guide))
  * Java(Runtime Environment JRE)
  * Selenium
  * Nightwatch
  * Chromedriver
1. Clone the repo
2. CD into the test folder
3. Run the config file you created to download the Selenium driver.
```
node nightwatch.conf.BASIC.js
```
4. Run tests
```
nightwatch --config nightwatch.conf.BASIC.js
```


### Tests
1. Verify title and body are rendering correctly.
2. Checks search functionalities from home page and details page forms.


## Built With

* [Flask](https://pypi.org/project/Flask/)
* [Google Maps API](https://developers.google.com/maps/documentation)
* [DarkSky API](https://darksky.net/dev/docs) - Weather Data
* Bootstrap ([1](https://startbootstrap.com/themes/grayscale/)|[2](https://startbootstrap.com/themes/sb-admin-2/))
