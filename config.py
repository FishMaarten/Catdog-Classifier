import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
os.environ["BASE_DIR"] = BASE_DIR

class Config(object):
    BASE_DIR = os.environ.get("BASE_DIR")
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret"
    UPLOAD_FOLDER = BASE_DIR + "uploads/"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
