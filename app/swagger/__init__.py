from urllib.parse import urlparse

from flask import Blueprint, current_app, jsonify, request, url_for
from flask_swagger import swagger

from ..__meta__ import __api_name__, __version__

swagger_bp = Blueprint('swagger', __name__)


@swagger_bp.route('/spec')
def spec():
    swag = swagger(current_app)

    swag['info']['version'] = __version__
    swag['info']['title'] = __api_name__
    swag['host'] = request.host
    swag['basePath'] = url_for('index', ).rstrip('/')

    o = urlparse(url_for('index', _external=True))

    swag['schemes'] = [o.scheme, ]
    swag['securityDefinitions'] = {
        'JWT': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Json Web Token 방식의 인증'
        }
    }

    return jsonify(swag)
