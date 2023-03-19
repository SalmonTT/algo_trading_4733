import pandas as pd
from DataDownloadFunctions import download_fx_data

# ----- FX Requests only -----
# available tickers: https://www.dukascopy.com/swiss/english/marketwatch/historical/
start_dt = '14 Jun 2016'
end_dt = '15 Jun 2016'
ticker = 'USDJPY'
output_path = 'data/'

tick_data = download_fx_data(start_dt, end_dt, ticker, output_path)

