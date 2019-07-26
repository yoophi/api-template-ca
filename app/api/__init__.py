from flask import Blueprint

api = Blueprint('api', __name__)

from app.api.sample import *  # noqa
from app.api.todo import *  # noqa
