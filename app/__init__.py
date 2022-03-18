from flask import Flask
from config import Config

myapp = Flask(__name__)
myapp.config.from_mapping(SECRET_KEY='password123')

from app import routes