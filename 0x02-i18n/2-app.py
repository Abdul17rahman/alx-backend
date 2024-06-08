#!/usr/bin/env python3
""" Basic flask app module"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, template_folder="./templates")
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Gets a default location"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Returns hello world"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
