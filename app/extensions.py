from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_mail import Mail

cors = CORS()
jwt = JWTManager()
ma = Marshmallow()
mail = Mail()


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    if identity == 'admin':
        return {
            'roles': ['admin', ]
        }
