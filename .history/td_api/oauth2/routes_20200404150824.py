from flask import Blueprint

oauth2_routes = Blueprint('oauth2', __name__, template_folder='templates', static_folder='static')

@oauth2_routes.route('/secondroute', methods=['GET'])
def hello1():
    return "sup1"

@oauth2_routes.route('/oauth_redirect', methods=['GET'])
def oauth_redirect(requests):
    return "sup_oauth_redirect"

@oauth2_routes.route('/oauth_callback', methods=['GET'])
def oauth_redirect(requests):
    return "sup_oauth_redirect"


