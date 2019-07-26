from flask import Flask
from flask import url_for, jsonify, request

from app.__meta__ import __api_name__, __version__
from app.config import config
from app.database import db
from app.extensions import cors, jwt, ma


def init_extensions(app):
    if app.config['REPO_ENGINE'] == 'MYSQL':
        db.init_app(app)

    cors.init_app(app, resources={r"/*": {"origins": "*"}, })
    jwt.init_app(app)
    ma.init_app(app)


def init_blueprint(app):
    @app.route('/')
    def index():
        """
        API 정보
        API 상세 정보
        ---
        tags:
          - User
        responses:
          200:
            description: OK
            schema:
              type: object
              properties:
                api_name:
                  type: string
                version:
                  type: string
                urls:
                  type: object
                  properties:
                    base:
                      type: string
                    health_check:
                      type: string
                    swagger:
                      type: string
        """
        return jsonify({
            'method': request.method,
            'api_name': __api_name__,
            'version': __version__,
            'urls': {
                'base': url_for('index', _external=True),
                'health_check': url_for('api.health_check', _external=True),
                'swagger': url_for('swagger.spec', _external=True),
            },
        })

    from app.api import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.admin import admin as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/api')

    from app.swagger import swagger_bp
    app.register_blueprint(swagger_bp, url_prefix='/swagger')


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    init_extensions(app)
    init_blueprint(app)

    return app
