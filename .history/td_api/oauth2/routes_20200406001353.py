from flask import Blueprint, request, redirect
from td_client.auth_utils import TDAuthSupport

oauth2_routes = Blueprint('oauth2', __name__, template_folder='templates', static_folder='static')

@oauth2_routes.route('/secondroute', methods=['GET'])
def hello1():
    import ipdb; ipdb.set_trace()
    return "sup1"

@oauth2_routes.route('/oauth_redirect', methods=['GET'])
def oauth_redirect():
    url = TDAuthSupport.get_oauth_redirect_url()
    return redirect(url)

@oauth2_routes.route('/oauth_callback', methods=['GET'])
def oauth_callback(request):
    return "sup_oauth_redirect"


