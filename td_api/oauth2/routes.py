import requests
from flask import Blueprint, request, redirect
from td_client.auth_utils import TDAuthSupport
from .models import db, OauthTokens
from datetime import datetime

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
        access_token = tokens_dict.get('access_token')
        refresh_token = tokens_dict.get('refresh_token')
        new_tokens = OauthTokens(
            access_token=access_token,
            refresh_token=refresh_token,
            created=datetime.now()
        )        
        db.session.add(new_tokens)
        db.session.commit()
        return "Tokens saved"
    
    return "Error saving tokens"
    


