from urllib import parse
from oauth2.models import db, OauthTokens
from datetime import datetime, timedelta
import requests

class TDAuthSupport:

    OAUTH_CALLBACK_URI = "https://localhost:8080/oauth_callback"
    TD_CLIENT_ID = "HWQ2GNZQECAF06ABTNR0PCRXO7OX2KON@AMER.OAUTHAP"
    TD_OAUTH_START_URL = f"https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={parse.quote(OAUTH_CALLBACK_URI)}&client_id={parse.quote(TD_CLIENT_ID)}"
    TD_ACCESS_TOKEN_VALID_MINUTES = 30  

    def __init__(self):
        return

    @classmethod
    def get_oauth_start_url(cls):
        return cls.TD_OAUTH_START_URL

    @classmethod
    def save_tokens(cls, tokens_dict, refreshing_tokens=False):
        access_token = tokens_dict.get('access_token')
        refresh_token = tokens_dict.get('refresh_token')
        tokens_obj=None
        # TODO make this logic more robust and handle errors
        if not refreshing_tokens and not len(OauthTokens.query.all()):
            new_tokens = OauthTokens(
                access_token=access_token,
                refresh_token=refresh_token,
                last_set_datetime=datetime.now()
            )
            db.session.add(new_tokens)
            tokens_obj=new_tokens
        else: 
            current_tokens = cls.get_current_tokens()
            current_tokens.access_token = access_token
            current_tokens.last_set_datetime = datetime.now()
            tokens_obj=current_tokens

        db.session.commit()

        return tokens_obj
    
    @classmethod
    def get_refreshed_tokens(cls):
        tokens = cls.get_current_tokens()
        refresh_token = tokens.refresh_token
        resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                        headers={'Content-Type': 'application/x-www-form-urlencoded'},
                        data={'grant_type': 'refresh_token',
                            'refresh_token': refresh_token,
                            'client_id': cls.TD_CLIENT_ID})
        if resp.ok:
            tokens_dict = resp.json()
            tokens_db_obj = TDAuthSupport.save_tokens(tokens_dict, refreshing_tokens=True)
            return tokens_db_obj
        
    @classmethod
    def get_current_tokens(cls):
        tokens = OauthTokens.query.first()
        return tokens if tokens else None
        
    @classmethod
    def get_valid_access_token(cls):
        
        if cls.access_token_expired():
            tokens = cls.get_refreshed_tokens()
            access_token = tokens.access_token
        else:
            access_token = cls.get_current_tokens().access_token
            
        return access_token
    
    @classmethod
    def access_token_expired(cls):
        token_expired = False
        
        current_tokens = cls.get_current_tokens()
        time_25_mins_ago = datetime.now() - timedelta(minutes=(cls.TD_ACCESS_TOKEN_VALID_MINUTES - 5))
        
        if current_tokens.last_set_datetime <= time_25_mins_ago:
            token_expired = True

        return token_expired
