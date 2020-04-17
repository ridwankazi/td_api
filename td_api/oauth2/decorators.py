from td_client.auth_utils import TDAuthSupport
from functools import wraps

def tokens_refreshed(func):
    
    @wraps(func)
    def decorator(*args, **kwargs):
        client_instance = args[0]
        access_token = TDAuthSupport.get_valid_access_token()
        client_instance.session.set_token(access_token)
        return func(*args, **kwargs)

    return decorator
