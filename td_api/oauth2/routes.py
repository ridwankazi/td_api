from flask import Blueprint


oauth2_routes = Blueprint('oauth2', __name__, template_folder='templates', static_folder='static')

@oauth2_routes.route('/secondroute', methods=['GET'])
def hello1():
    return "sup1"


