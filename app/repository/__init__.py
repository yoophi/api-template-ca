from flask import current_app
from werkzeug.local import LocalProxy

from app.repository.memory import MemRepo
from app.repository.sqla import SqlaRepo

repo_mappings = {
    'MYSQL': SqlaRepo,
    'MEMORY': MemRepo,
}


def get_repo():
    cls = repo_mappings.get(current_app.config["REPO_ENGINE"], MemRepo)
    return cls()


current_repo = LocalProxy(get_repo)
