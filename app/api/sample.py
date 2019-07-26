from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required, get_raw_jwt, create_access_token

from app.api import api
from app.database import db
from app.models import User


@api.route('/health_check')
def health_check():
    return jsonify({'ok': True})


@api.route('/v1.0/public')
def public():
    return jsonify({'ok': True})


@api.route('/v1.0/private')
@jwt_required
def private():
    data = get_raw_jwt()
    return jsonify(data)


@api.route('/v1.0/login', methods=['POST', ])
def login():
    username = request.json.get('username', None)
    return jsonify({
        'access_token': create_access_token(identity=username, )
    })


@api.route('/v1.0/db')
def db_test():
    count = db.session.query(User).count()
    return jsonify({
        'count': count
    })


@api.route('/error')
def error():
    return 999 / 0


@api.route('/log-error')
def log_error():
    current_app.logger.error('log-error')
    return 'log-error'


@api.route('/handle-error')
def handle_error():
    try:
        rv = 1 / 0
        return jsonify(rv=rv)
    except:
        current_app.logger.exception('handle-error')
        return jsonify(error=True)


@api.route('/log-test')
def log_test():
    current_app.logger.info('info')
    current_app.logger.debug('debug')
    current_app.logger.error('error')
    try:
        rv = 10 / 0
    except:
        current_app.logger.exception('exception')

    return 'log-test'
