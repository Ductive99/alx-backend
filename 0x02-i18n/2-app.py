#!/usr/bin/env python3
"""Task 0: basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Defines the languages available for our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """Determines the best match with the available languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """returns the index page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)