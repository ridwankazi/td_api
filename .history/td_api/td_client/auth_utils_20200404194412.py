
class TDAuthSupport:

    OAUTH_CALLBACK_URI = "http://localhost:8080/oauth_callback"    
    TD_CLIENT_ID = "7S9ZS56UOPUINAPAFII1VMEXBZLFW82U"
    TD_OAUTH_REDIRECT_URL = f"https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={OAUTH_CALLBACK_URI}&client_id={TD_CLIENT_ID}%40AMER.OAUTHAP"

    @classmethod
    def get_oauth_redirect_url(cls):
        return cls.TD_OAUTH_REDIRECT_URL
