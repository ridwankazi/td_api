from flask import Blueprint, request, redirect
from td_client.auth_utils import TDAuthSupport
from datetime import datetime
import requests

oauth2_routes = Blueprint('oauth2', __name__, template_folder='templates', static_folder='static')

@oauth2_routes.route('/secondroute', methods=['GET'])
def hello1():
    TDAuthSupport.get_refreshed_tokens()
    return "sup1"

@oauth2_routes.route('/oauth_start', methods=['GET'])
def oauth_start():
    url = TDAuthSupport.get_oauth_start_url()
    return redirect(url)

@oauth2_routes.route('/oauth_callback', methods=['GET'])
def oauth_callback():

    code = request.args.get('code')

    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                        headers={'Content-Type': 'application/x-www-form-urlencoded'},
                        data={'grant_type': 'authorization_code',
                            'refresh_token': '',
                            'access_type': 'offline',
                            'code': code,
                            'client_id': TDAuthSupport.TD_CLIENT_ID,
                            'redirect_uri': TDAuthSupport.OAUTH_CALLBACK_URI})

    if resp.ok:
        tokens_dict = resp.json()
        TDAuthSupport.save_tokens(tokens_dict)
        return "Tokens saved"
    
    return "Error saving tokens"
    


