import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "CHANGE ME"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STM_API_KEY = os.environ["STM_API_KEY"]


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


config = {"development": DevelopmentConfig}
