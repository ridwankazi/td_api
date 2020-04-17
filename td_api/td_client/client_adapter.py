from tdameritrade import TDClient
from .auth_utils import TDAuthSupport
from oauth2.decorators import tokens_refreshed

class TDClientAdapter(TDClient):

    def __init__(self):
        access_token = TDAuthSupport.get_valid_access_token()
        super().__init__(access_token)
    
    @tokens_refreshed
    def get_options_chain(self, *args, **kwargs):
        
        return self.options(*args, **kwargs)