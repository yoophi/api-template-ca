from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

cors = CORS()
jwt = JWTManager()
ma = Marshmallow()


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    if identity == 'admin':
        return {
            'roles': ['admin', ]
        }
