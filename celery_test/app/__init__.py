from celery import Celery
from flask import Flask

celery_app = Celery(__name__, broker='redis://localhost:6379/1')

flask_app = Flask(__name__)

from app import routes