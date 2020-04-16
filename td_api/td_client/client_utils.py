from tdameritrade import TDClient
from .auth_utils import TDAuthSupport

class TDClientAdapter(TDClient):

    def __init__(self):
        access_token = TDAuthSupport.get_valid_access_token()
        super().__init__(access_token)
    
    