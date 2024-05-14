# Packages
import talisker.requests
import requests
import flask
import jinja2
from canonicalwebteam.flask_base.app import FlaskBase


app = FlaskBase(
    __name__,
    "0.0.0.0",
    template_folder="../templates",
    static_folder="../templates/static",
)
session = talisker.requests.get_session()

@app.route("/")
def contribute_index():
    return flask.make_response(
        flask.render_template(
            "index.html"
        )
    )
