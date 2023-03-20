# !pip install findatapy
import pandas as pd
import os
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

def download_with_node(ticker_list, start_dt, end_dt, timeframe, directory):
    """
        - downloads .csv file for every ticker in the ticker_list in the specified directory
        - https://www.dukascopy-node.app/config/cli for documentation on CLI command
    """
    for ticker in ticker_list:
        # check if data is already downloaded
        file_name = f"{directory}/{ticker}-{timeframe}-{start_dt}-{end_dt}.csv"
        if os.path.isfile(file_name):
            continue
        else:
            # generate command line request
            cli_command = f'npx dukascopy-node -i {ticker} -from {start_dt} -to {end_dt} ' \
                          f'-t {timeframe} -v true -f csv -dir {directory} -bp 1000'
            # enter cli command to download data
            os.system(cli_command)

    print(f'downloaded {ticker_list}')
    pass




