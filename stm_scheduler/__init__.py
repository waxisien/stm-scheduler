from flask import Blueprint, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from .config import config
from .schedule import get_schedule

db = SQLAlchemy()

main = Blueprint("main_app", __name__)


@main.route("/line/<line_id>/stop/<stop_id>")
def index(line_id, stop_id):
    schedule = get_schedule(line_id, stop_id)
    return jsonify(schedule)


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    app.register_blueprint(main)

    return app
