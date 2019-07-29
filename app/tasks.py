from . import create_celery

celery = create_celery()

from app.main.tasks import *
