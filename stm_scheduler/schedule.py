from datetime import datetime

from flask import current_app
from google.transit import gtfs_realtime_pb2
import requests

STM_GTFS_URL = "https://api.stm.info/pub/od/gtfs-rt/ic/v1/tripUpdates"


def get_schedule(line_id, stop_id):
    headers = {"apikey": current_app.config["STM_API_KEY"]}
    response = requests.post(STM_GTFS_URL, headers=headers)

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
