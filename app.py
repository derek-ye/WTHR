import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    """ Page at '/' """

    # no 'templates/' before file -> Flask auto checks 'templates' folder
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.debug=True
    app.run()