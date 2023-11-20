# app.py
from flask import Flask
from core.config import DevConfig
from core.db import db
from api.route.auth import auth_route as auth
from api.route.user import user_route as user
from api.route.api import general_route as general

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(general)
app.register_blueprint(user)


if __name__ == '__main__':
    app.run(debug=True)
