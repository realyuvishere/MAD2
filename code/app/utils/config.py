import os
basedir = os.path.abspath(os.path.dirname(__file__))


class FlaskConfig:
    DEBUG = False
    API_PREFIX='/api/v1'
    SQLITE_DB_DIR = os.path.join(basedir, "../../db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "db.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "thisissecter"
    SECURITY_PASSWORD_SALT = "thisissaltt"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 3

class CeleryConfig:
    broker_url = "redis://localhost:6379/1"
    result_backend = "redis://localhost:6379/2"
    timezone = "Asia/kolkata"
    broker_connection_retry_on_startup = True

class MailConfig:
    SMTP_HOST = "localhost"
    SMTP_PORT = 1025
    SENDER_EMAIL = '21f3000180@ds.study.iitm.ac.in'
    SENDER_PASSWORD = ''