from flask import Blueprint, Flask, jsonify

from stm_scheduler.config import config
from stm_scheduler.extensions import cache
from stm_scheduler.schedule import get_schedule

main = Blueprint("main_app", __name__)


@main.route("/line/<line_id>/stop/<stop_id>")
def index(line_id, stop_id):
    schedule = get_schedule(line_id, stop_id)
    return jsonify(schedule)


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    cache.init_app(app)

    app.register_blueprint(main)

    return app
