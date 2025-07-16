from flask import Blueprint, request, jsonify
from .models import User
from . import db

# Utility function to create a standardized API response
def api_response(status_code, message, data=None):
    response = {
        'status_code': status_code,
        'message': message,
        'data': data
    }
    return jsonify(response), status_code

bp = Blueprint('api', __name__, url_prefix='/api')

# [GET] /api/users
@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return api_response(200, "Data semua user berhasil diambil.", users_data)

# [GET] /api/users/<id>
@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return api_response(404, f"User dengan ID {id} tidak ditemukan.")
    
    return api_response(200, f"Data user dengan ID {id} berhasil diambil.", user.to_dict())

# [POST] /api/users
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password') or not data.get('name') or not data.get('username'):
        return api_response(400, "Data yang dikirim tidak lengkap.")
    
    if User.query.filter_by(email=data['email']).first():
        return api_response(409, "Email sudah terdaftar.")
        
    if User.query.filter_by(username=data['username']).first():
        return api_response(409, "Username sudah terdaftar.")

    new_user = User(
        name=data['name'],
        email=data['email'],
        username=data['username']
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return api_response(201, "User berhasil dibuat.", new_user.to_dict())

# [PUT] /api/users/<id>
@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return api_response(404, f"User dengan ID {id} tidak ditemukan.")

    data = request.get_json()
    
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.username = data.get('username', user.username)

    if 'password' in data and data['password']:
        user.set_password(data['password'])

    db.session.commit()
    return api_response(200, f"User {user.username} berhasil diupdate.", user.to_dict())

# [DELETE] /api/users/<id>
@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return api_response(404, f"User dengan ID {id} tidak ditemukan.")

    db.session.delete(user)
    db.session.commit()
    return api_response(200, f"User dengan ID {id} berhasil dihapus.")

# [POST] /api/login
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return api_response(400, "Email dan password diperlukan.")
        
    user = User.query.filter_by(email=data.get('email')).first()

    if user is None or not user.check_password(data.get('password')):
        return api_response(401, "Email atau password salah.")

    return api_response(200, "Login berhasil.", user.to_dict())
