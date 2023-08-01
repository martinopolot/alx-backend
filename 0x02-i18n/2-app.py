#!/usr/bin/env python3
""" Starter Flask app, Basic Babel setup, get locale from request """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
""" instantiates the Babel object """


class Config(object):
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Uses that class as config for Flask app """


@app.route('/')
def root():
    """ starter Flask app """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """ etermining the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
