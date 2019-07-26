from flask import jsonify
from flask_jwt_extended import jwt_required

from app.admin import admin
from app.decorators import jwt_role_required


@admin.route('/v1.0/admin/sample')
@jwt_required
@jwt_role_required('admin')
def sample():
    return jsonify({'ok': True})
