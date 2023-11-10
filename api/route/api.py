from flask import Blueprint

general = Blueprint('general', __name__)


@general.route('/', methods=['GET'])
def hello():
    return 'Hello, Flask!'
