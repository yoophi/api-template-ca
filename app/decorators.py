from functools import wraps

from flask_jwt_extended import get_jwt_claims


def jwt_role_required(*args):
    required_roles = args

    def f(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            claims = get_jwt_claims()
            user_roles = claims.get('roles', [])
            for role in required_roles:
                if role not in user_roles:
                    raise Exception(f'{role} not in {user_roles}')

            return fn(*args, **kwargs)

        return wrapper

    return f