import os


class Config:
    # DEBUG = True
    # TESTING = False
    # CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret-key"
    # SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
