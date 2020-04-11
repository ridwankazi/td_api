from urllib import parse
class TDAuthSupport:

    OAUTH_CALLBACK_URI = "https://localhost:8080/oauth_callback"
    TD_CLIENT_ID = "HWQ2GNZQECAF06ABTNR0PCRXO7OX2KON@AMER.OAUTHAP"
    TD_OAUTH_REDIRECT_URL = f"https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={parse.quote(OAUTH_CALLBACK_URI)}&client_id={parse.quote(TD_CLIENT_ID)}"

    @classmethod
    def get_oauth_redirect_url(cls):
        return cls.TD_OAUTH_REDIRECT_URL

    