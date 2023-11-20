from flask import Blueprint

general_route = Blueprint('general', __name__)


@general_route.route('/', methods=['GET'])
def hello():
    return 'Hello, Flask!'
