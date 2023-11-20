# auth.py
import jwt
import os
from flask import request, jsonify
from functools import wraps
from api.model.User import User


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return {'message' : 'You are not authorized !!'}, 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
            current_user = User.query\
                .filter_by(email = data['email'])\
                .first()
        except Exception as e:
            print(e)
            return {'message' : 'Token is invalid !!'}, 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated
