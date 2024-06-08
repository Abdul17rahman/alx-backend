#!/usr/bin/env python3
""" Basic flask app module"""


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__, template_folder="./templates")
babel = Babel(app)


class Config:
    LANGAUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ Returns hello world"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
