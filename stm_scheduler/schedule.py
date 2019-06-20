from datetime import datetime

from flask import current_app
from google.transit import gtfs_realtime_pb2
import requests

from stm_scheduler.extensions import cache

# sandbox API is limited to 1000 call per day
GTFS_API_CACHE = 120

@cache.cached(timeout=GTFS_API_CACHE)
def get_schedule(line_id, stop_id):
    headers = {"apikey": current_app.config["STM_GTFS_API_KEY"]}
    response = requests.post(current_app.config["STM_GTFS_API_URL"], headers=headers)

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)

    dates = []
    for entity in feed.entity:
        if entity.trip_update.trip.route_id == line_id:
            for stop_time_update in entity.trip_update.stop_time_update:
                if stop_time_update.stop_id == stop_id and stop_time_update.HasField(
                    "arrival"
                ):
                    dates.append(datetime.fromtimestamp(stop_time_update.arrival.time))

    dates.sort()
    return dates
