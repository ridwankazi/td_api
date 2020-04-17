
class OptionsSupport:

    @classmethod
    def volume_sorted_contracts(cls, prices_dict):
        return {k:v for k,v in sorted(prices_dict.items(), key=lambda item: item[1][0]['totalVolume'], reverse=True)}

    @classmethod
    def open_interest_sorted_contracts(cls, prices_dict):
        return {k:v for k,v in sorted(prices_dict.items(), key=lambda item: item[1][0]['openInterest'], reverse=True)}
        
    @classmethod
    def get_top_ten_prices(cls,prices_dict):
        return list(prices_dict.keys())[0:10]

    @classmethod
    def make_summary_dict(cls,contract_dict):
        return {
            "strike": contract_dict.get('strikePrice'),
            "volume": contract_dict.get('totalVolume'),
            "open_interest": contract_dict.get('openInterest'),
            "bid": contract_dict.get('bid'),
            "ask": contract_dict.get('ask'),
            "market": contract_dict.get('mark'),
        }
    
    @classmethod
    def make_summary_list(cls,prices_dict, prices_list):
        return [cls.make_summary_dict(prices_dict.get(price)[0]) for price in prices_list]

    @classmethod
    def days_to_expiration(cls, option_expiration_date_str):
        return int(option_expiration_date_str.split(':')[1])

