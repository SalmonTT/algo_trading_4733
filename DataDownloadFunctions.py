# !pip install findatapy
import pandas as pd
import os.path
from findatapy.market import Market, MarketDataRequest, MarketDataGenerator

def download_fx_data(start_dt, end_dt, ticker, output_path):
    # check if file already exists
    start_dt_string = pd.to_datetime(start_dt).strftime("%m-%d-%Y")
    end_dt_string = pd.to_datetime(end_dt).strftime("%m-%d-%Y")
    file_name = output_path + ticker + '_' + start_dt_string + '_' + end_dt_string + '.pkl'
    if os.path.isfile(file_name):
        print(file_name + ' found locally!')
        return pd.read_pickle(file_name)
    else:
        market = Market(market_data_generator=MarketDataGenerator())
        # generate request
        fx_request = MarketDataRequest(start_date=start_dt, finish_date=end_dt,
                                       category='fx', fields=['bid', 'ask', 'bidv', 'askv'], freq='tick',
                                       data_source='dukascopy', tickers=[ticker])
        # download data
        tick_data = market.fetch_market(fx_request)
        tick_data.to_pickle(file_name)
        print(file_name + ' downloaded!')
    return tick_data


