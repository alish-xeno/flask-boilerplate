# Description: Auth routes
from flask import request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
import os
from dotenv import load_dotenv
load_dotenv()

from api.model.User import User
from api.schema.user import UserSchema


auth_route = Blueprint('auth', __name__, url_prefix='/api/auth')


# register route
@auth_route.route('/register', methods =['POST'])
def register():
    # creates a dictionary of the json data
    data = request.get_json()

    # Check if all required fields are present
    required_fields = ['username', 'email', 'password']
    # return error saying field 'x' is missing, if any of the required fields are missing
    for field in required_fields:
        if field not in data:
            return {'message': f"{field} field is missing"}, 400

    # gets name, email and password
    username, email = data.get('username'), data.get('email')
    password = data.get('password')
  
    # checking for existing user
    if User.query.filter_by(email=email).first():
        return {'message': 'Email already exists'}, 400
    
    if User.query.filter_by(username=username).first():
        return {'message': 'Username already exists'}, 400

    # database ORM object
    user = User(
        username = username,
        email = email,
        password = generate_password_hash(password)
    )
    # insert user
    user.save()

    return UserSchema().jsonify(user), 201


# login route
@auth_route.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    auth = request.get_json()

    required_fields = ['email', 'password']
    # return error saying field 'x' is missing, if any of the required fields are missing
    for field in required_fields:
        if field not in auth:
            return {'message': f"{field} field is missing"}, 400
  
    user = User.query.filter_by(email=auth.get('email')).first()
  
    if not user:
        # returns 401 if user does not exist
        return {'message': 'User does not exist'}, 401
  
    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'email' : user.email,
        }, os.getenv('SECRET_KEY'), algorithm="HS256")

        return {'token' : token, 'user': UserSchema().jsonify(user)}
    # returns 403 if password is wrong
    return {'message': 'Could not verify'}, 403