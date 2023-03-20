from DataDownloadFunctions import download_fx_data, download_with_node

# ----- Global config ----- #
# print(os.getcwd()) to get the current directory of this .py file
# output_path should be the "data" folder in your project directory
output_path = '/Users/simon/Documents/GitHub/algo_trading_4733/data'

# ----- Download FX tick data using findatapy ----- #
"""
    - Can only download FX tick data
    - https://www.dukascopy.com/swiss/english/marketwatch/historical/
"""
# date has to be in the following format
start_dt = '14 Jun 2016'
end_dt = '15 Jun 2016'
# ticker has to be FX pairs
ticker = 'USDJPY'
# call download function
tick_data = download_fx_data(start_dt, end_dt, ticker, output_path)

# ----- Node js download ----- #
"""
    - Download from Dukascopy using a Node js library
    - Able to download all assets available from Dukascopy
    - https://www.dukascopy.com/swiss/english/marketwatch/historical/
"""
# date has to be in the following format
start_dt = '2023-01-02'
end_dt = '2023-01-03'
timeframe = 'tick'
tickers = ['btcusd', 'ethusd', 'aaplususd', 'tslaususd', 'eurusd']
# call function to download csv files to the output_path
download_with_node(tickers, start_dt, end_dt, timeframe, output_path)

