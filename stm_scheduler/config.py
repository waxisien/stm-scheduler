import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "CHANGE ME"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STM_GTFS_API_KEY = os.environ["STM_API_KEY"]
    STM_GTFS_API_URL = "https://api.stm.info/pub/od/gtfs-rt/ic/v1/tripUpdates"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


config = {"development": DevelopmentConfig}
