# service.py
from api.model.User import User
from api.schema.user import UserSchema


def index():
    users = User.query.all()

    return UserSchema(many=True).jsonify(users)


def store(username, email, password):
    user = User(username=username, email=email, password=password)

    if User.query.filter_by(email=user.email).first():
        return {'message': 'Email already exists'}, 400
    
    if User.query.filter_by(username=user.username).first():
        return {'message': 'Username already exists'}, 400

    user.save()

    return UserSchema().jsonify(user)


def show(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return {'message': 'User not found'}, 404

    return UserSchema().jsonify(user)


def update(user_id, username, email):
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404

    if User.query.filter(User.id != user_id).filter_by(email=email).first():
        return {'message': 'Email already exists'}, 400

    if User.query.filter(User.id != user_id).filter_by(username=username).first():
        return {'message': 'Username already exists'}, 400

    user.save()
    return UserSchema().jsonify(user)


def destroy(user_id):
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404

    user.delete()
    return UserSchema().jsonify(user)
