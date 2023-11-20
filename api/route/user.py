from flask import Blueprint, request
from api.utils.auth import token_required

from api.service import user as user_service

user_route = Blueprint(
    'user',
    __name__,
    url_prefix='/api'
)


@user_route.route('/users', methods=['GET'])
def list():
    users = user_service.index()

    return users


@user_route.route('/users/<int:user_id>', methods=['GET'])
@token_required
def get(current_user, user_id):
    user = user_service.show(user_id)
    return user



@user_route.route('/users', methods=['POST'])
def create():
    user = user_service.store(
        username=request.json['username'],
        email=request.json['email'],
        password=request.json['password']
    )

    return user


@user_route.route('/users/<int:user_id>', methods=['PUT'])
def edit(user_id):
    user = user_service.update(
        user_id=user_id,
        username=request.json['username'],
        email=request.json['email']
    )

    return user


@user_route.route('/users/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    user = user_service.destroy(user_id)

    return user
