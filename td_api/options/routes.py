from flask import Blueprint, request, redirect
from td_client.auth_utils import TDAuthSupport
from td_client.client_adapter import TDClientAdapter
from .options_support import OptionsSupport
from datetime import datetime
import requests
import json 

options_routes = Blueprint('options', __name__, template_folder='templates', static_folder='static')

@options_routes.route('/options_summary', methods=['GET'])
def options_summary():
    
    ticker_symbol = request.args.get('ticker')

    td_c = TDClientAdapter()
    options_chain = td_c.get_options_chain(ticker_symbol)

    call_expiration_date_map = options_chain.get('callExpDateMap')
    put_expiration_date_map = options_chain.get('putExpDateMap')

    calls_summary_dict = {"volume": {}, "open_interest": {}}
    puts_summary_dict = {"volume": {}, "open_interest": {}}

    for exp_date, prices_dict in call_expiration_date_map.items():
        if OptionsSupport.days_to_expiration(exp_date) > 1:
            vol_sorted_contracts = OptionsSupport.sorted_contracts_by('totalVolume', prices_dict)
            oi_sorted_contracts = OptionsSupport.sorted_contracts_by('openInterest', prices_dict)

            top_ten_prices_volume = OptionsSupport.get_top_ten_prices(vol_sorted_contracts)
            top_ten_prices_oi = OptionsSupport.get_top_ten_prices(oi_sorted_contracts)
            
            calls_summary_dict['volume'][exp_date] = OptionsSupport.make_summary_list(vol_sorted_contracts, top_ten_prices_volume)
            calls_summary_dict['open_interest'][exp_date] = OptionsSupport.make_summary_list(oi_sorted_contracts, top_ten_prices_oi)

    for exp_date, prices_dict in put_expiration_date_map.items():
        if OptionsSupport.days_to_expiration(exp_date) > 1:
            vol_sorted_contracts = OptionsSupport.sorted_contracts_by('totalVolume', prices_dict)
            oi_sorted_contracts = OptionsSupport.sorted_contracts_by('openInterest', prices_dict)

            top_ten_prices_volume = OptionsSupport.get_top_ten_prices(vol_sorted_contracts)
            top_ten_prices_oi = OptionsSupport.get_top_ten_prices(oi_sorted_contracts)
            
            puts_summary_dict['volume'][exp_date] = OptionsSupport.make_summary_list(vol_sorted_contracts, top_ten_prices_volume)
            puts_summary_dict['open_interest'][exp_date] = OptionsSupport.make_summary_list(oi_sorted_contracts, top_ten_prices_oi)

    calls_highest_volume_contracts_accross_dates = OptionsSupport.highest_summary_dicts_accross_dates_by('volume', calls_summary_dict['volume'])
    calls_highest_open_interest_contracts_accross_dates = OptionsSupport.highest_summary_dicts_accross_dates_by('open_interest', calls_summary_dict['open_interest'])
    
    puts_highest_volume_contracts_accross_dates = OptionsSupport.highest_summary_dicts_accross_dates_by('volume', puts_summary_dict['volume'])
    puts_highest_open_interest_contracts_accross_dates = OptionsSupport.highest_summary_dicts_accross_dates_by('open_interest', puts_summary_dict['open_interest'])

    return json.dumps({"calls_highest_volume_contracts_accross_dates": calls_highest_volume_contracts_accross_dates,
                       "calls_highest_open_interest_contracts_accross_dates": calls_highest_open_interest_contracts_accross_dates, 
                       "puts_highest_volume_contracts_accross_dates": puts_highest_volume_contracts_accross_dates, 
                       "puts_highest_open_interest_contracts_accross_dates": puts_highest_open_interest_contracts_accross_dates, 
                       "calls": calls_summary_dict, 
                       "puts": puts_summary_dict})

