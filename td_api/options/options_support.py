
class OptionsSupport:

    @classmethod
    def sorted_contracts_by(cls, desired_sorting_field, prices_dict):
        return {k:v for k,v in sorted(prices_dict.items(), key=lambda item: item[1][0][desired_sorting_field], reverse=True)}

    @classmethod
    def highest_summary_dicts_accross_dates_by(cls, summary_dict_field,summary_dict):
        return {k:v[0] for k,v in sorted(summary_dict.items(), key=lambda item: item[1][0][summary_dict_field], reverse=True)}
        
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

