from flask import Blueprint, request, jsonify
from app.models import User, db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email']) # type: ignore
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'username': new_user.username}), 201
