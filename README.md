# algo_trading_4733

**Note**: Please create a folder called "data" locally to store data. Anything in the folder "data" will not be uploaded to github (including 
the folder itself).

Developing and Evaluating Intraday Trading Strategies Using Market Data

In this project, you will develop and evaluate intraday trading strategies using market data from a simulated intraday market data. 
You will have the flexibility to choose your own data source, such as stock prices, currency exchange rates, or commodity prices, 
and develop their own trading strategy based on technical analysis or machine learning techniques.

The project will consist of three main stages:

## Stage 1: Data Acquisition and Preprocessing
You will collect and preprocess intraday market data from a random generator or from a selected financial instrument or market using  Python. 
The data should include time series of price, volume, and other relevant market variables.  
Two market generators are provided (mkdata.py and mkdata2.py) and both generate microsecond data with the following columns:
```
'Timestamp': timestamps,
'Bid Price': bid_prices,
'Bid Quantity': bid_quantities,
'Offer Price': offer_prices,
'Offer Quantity': offer_quantities
```
### Distinction between types of market data:
There are 3 types of market data that could potentially be referred to as tick data:
- Trade or Time-and-Sales data 
  - Fields: ```['timestamp', 'price', 'volume', 'direction', 'venue]'```
  - Each tick represents a trade
- Quote data:
  - Fields: ```['timestamp', 'Bid Price', 'Bid Size', 'Ask Price', 'Ask Size']```
  - Each tick represents a new quote (either ask or bid)
- FIX messages:
  - You can revisit the horrors of Q1 Midterm to refresh your memory of FIX messages

The market data generator provided by prof. Donadio is actually a quote data generator. Tick data
referred in the book my Marcos de Lopez is actually trade data (each tick represents a trade).  

The question becomes: **How do we use the same methods described in Lopez's book to transform quote data?**  

In the next section I will document the different data sources and what kind of market data they offer.  

Resources:
- [Cleaning Tick and Quote Data](https://machinefactor.tech/blog/cleaning-tick-and-quote-data-1)
- [Understanding Good Quality FX Tick Data](https://tradermade.com/blog/understanding-good-quality-fx-tick-data)
- [Quote bars for US Equities](https://www.tickdata.com/product/quote-bars/)
- [How to Match Trades and Quotes for NYSE Stocks - 2005](https://lirias.kuleuven.be/retrieve/323063)
  - How to merge trades and quotes datasets (each with their own timestamp)
- [How to get the most out of US equitiy market data - 2022](https://sander.schwenk-nebbe.com/2021/12/how-to-get-the-most-out-of-us-equity-market-data)
## Data Sources:
[TrueFX](https://www.truefx.com/): 
- Quote data of currency pairs. 
- Note that for currency pairs, there are no volume data available due to the scale of the market. You can only
obtain timestamp, bid price and ask price. 

[Dukascopy](https://www.dukascopy.com/swiss/english/marketwatch/historical/):
- Quote data for almost everything (daily download only)
- 3 methods to download data from Dukascopy:
  1. From their website. 
     - pros: can download quote data of any listed assets
     - cons: can only download one day of quote data
  2. Using the function download_fx_data from DataDownloadFunctions.py
     - pros: can specify date range
     - cons: can only download FX pairs
  3. Using [dukascopy-node](https://www.dukascopy-node.app/):
     - pros: can download pretty much anny assets, can also specify date range
     - cons: a bit tricky to set up
     - Set-up:
       1. install node.js via https://nodejs.dev/en/download/
       2. go to terminal and install the library using: ```npm install dukascopy-node --save```
       3. go to [this awesome website](https://www.dukascopy-node.app/instruments) to get instructions on
       downloading different asset's quote data. An example for AAPL quote data is:
       ```npx dukascopy-node -i aaplususd -from 2023-01-01 -to 2023-01-12 -t m1 -f csv``` A csv file will be saved
       at your download folder (on MacOS it is saved under user/download rather than your usual Download)

[Polygon.io](https://polygon.io/)
- To access trades data $79/month
- To access trades and quotes data $200/month

[BitMex exchange](https://public.bitmex.com/?prefix=data)
- Free Trades and Quotes data from the BitMex exchange
- Includes multiple crypto assets
- So far can only manually download daily .csv files

## Stage 2: Create Bar Data
You will create bar data and explain the different kind of bar data you managed to create.  
### Motivation:
- How to deal with the irregularities of the arrival of bars is the focus of this stage.
- This stage follows Chapter 2 from Marcos de Lopez's *Advances in Financial Machine Learning*.

### Types of bar data:
#### Standard Bars:
Given that these bars arrive at irregular frequencies, we call this series of bars inhomogeneous series. 
Standard bars transform them from inhomogeneous series to homogeneous series derived from regular sampling.  

Includes: ```['timestamp', 'vwap', 'open', 'close', 'high', 'low', 'volume']```
- **Time Bars (avoid)**:
  - Obtained by sampling information at fixed time intervals (e.g. minute):
  - Should be avoided for two reasons:
    1. markets do not process information at constant time interval. Time bars can easily 
    oversample information during low-activity periods and undersample information during high-activity periods 
    (think Black Monday).
    2. Time-sampled series often exhibit poor statistical properties (serial correlation, heteroscedasticity and 
    non-normality of returns).
- **Tick Bars**:
  - Instead of sampling at constant time interval, sample at constant number of transactions (e.g. 1,000 ticks).
  - Pros: 
    - Sampling as a function of number of transactions exhibited desirable statistical properties (Gaussian).
  - Cons: 
    - Subject to outliers due to certain behaviors from exchanges during conclusion of auctions. 
    - Each transaction could differ in volume (e.g. 10 transactions each of size 1 vs. 10 transactions each of size
    1,000).
- **Volume Bars**:
  - Sampling every time a pre-defined amount of the security's unites (shares, futures contracts, etc.) have been 
  exchanged.
  - Mitigates the size of transaction issue presented in tick bars. Therefore, should be preferred over tick bar.
- **Dollar Bars**:
  - Sample an observation every time a pre-defined market value is exchanged (generally in terms of USD for currency
  pairs). Alternative, could also sample as a function of free-floating market capitalization of a company (stocks) or
  the outstanding amount of issued debt (fixed income). For currency, perhaps as a function of monetary supply?
  - Pros: 
    - Given that the number of outstanding shares often changes multiple times throughout the course of a security's 
    life (due to corporate actions such as buybacks), dollar bars are robust in the face of these actions.
#### Information-Driven Bars:
The purpose of info-driven bars is to sample more frequently when new information arrives to the market.
- **Tick Imbalance Bars**:
- **Tick Runs Bars**:
- **Volume/Dollar Runs Bars**:

## Stage 3: Trading Strategy Development
Based on the intraday market data, students will develop their own trading strategy using 
technical analysis or machine learning techniques. The strategy should be able to generate buy or sell signals based on the market data, 
and the trading decisions should be backtested on historical data.  

### List of papers to reference:  
"Intraday technical analysis of individual stocks using machine learning techniques" by Marjan Jalali, Reza Malekipirbazari, and Jafar Razmi. 
- This paper explores the use of machine learning techniques for intraday technical analysis of individual stocks, 
and evaluates the performance of various machine learning algorithms in predicting intraday stock price movements.

"Machine Learning and Statistical Arbitrage in High-Frequency Trading" by Marcos López de Prado. 
- This paper explores the use of machine learning and statistical arbitrage techniques for intraday trading of stocks and other financial instruments.

"Intraday momentum trading strategies" by David Easley, Marcos López de Prado, and Maureen O'Hara. 
- This paper examines the profitability of intraday momentum trading strategies using high-frequency data, 
and compares the performance of various momentum indicators and trading rules.

"A high-frequency trading strategy based on machine learning using RNN and SVM" by Soyoung Kim, Jiwon Jang, and Jaehun Lee. 
- This paper proposes a high-frequency trading strategy based on machine learning using recurrent neural networks (RNN) and 
support vector machines (SVM), and evaluates its performance using intraday data from the Korean stock market.

"Intraday technical analysis and trading strategies" by Markos Katsanos. 
- This book provides an overview of intraday technical analysis and trading strategies, 
including momentum, mean reversion, and breakout strategies, and provides code examples in MATLAB.

"A neural network-based trading system for intraday stock prices" by Kuan-Pin Lin and Tzu-Yi Yang. 
- This paper proposes a neural network-based trading system for intraday stock prices, 
and evaluates its performance using intraday data from the Taiwan stock market.

"Intraday trading strategies for crude oil futures" by Giovanni Urga and Gabriele Fiorentini. 
- This paper examines the profitability of intraday trading strategies for crude oil futures, 
and compares the performance of various trading rules and technical analysis indicators.

"Using news articles to predict intraday stock price movements" by Martijn M. Boons and Mark D. Flood. 
- This paper proposes a news-based trading strategy that uses sentiment and event information extracted from news articles 
to predict intraday stock price movements, and evaluates its performance using intraday data from the New York Stock Exchange.

"Intraday trading strategies in the foreign exchange market" by James Chen and Mark Sebastian. 
- This book provides an overview of intraday trading strategies in the foreign exchange market, 
including trend following, mean reversion, and breakout strategies, and provides code examples in Python.

"Trading the opening bell: An analysis of intraday patterns and trading strategies" by Markus Baltzer and Thorsten Hens. 
- This paper examines intraday patterns in stock returns around the opening bell, 
and evaluates the profitability of various trading strategies based on these patterns.

"Intraday trading strategies for the S&P 500 index futures market" by José G. García, Vicente Meneu, and Javier Ruiz. 
- This paper explores the profitability of intraday trading strategies for the S&P 500 index futures market, 
and compares the performance of various trading rules and technical analysis indicators.

## The deliverables of this project:

Code to be submitted to canvas.  

And you will submit the presentation following these slides (this is just to give you an idea, you can have less, more slides, you can talk about something different)

Slide 1: Title and Introduction - Introduction to the project and outline of the presentation. Don't forget your team members.

Slide 2: Motivation - Briefly discuss the motivation behind the project and the importance of intraday trading strategies.

Slide 3: Data Acquisition and Preprocessing - Discuss the data source and how the data was acquired and preprocessed for analysis.

Slide 4: Exploratory Data Analysis - Present visualizations and summary statistics of the intraday market data, including the distribution of prices, volume, and other relevant market variables. You will take an additional slides to talk about the bar data.

Slide 5: Technical Analysis or Machine Learning Techniques - Describe the technical analysis or machine learning techniques used to develop the trading strategy.

Slide 6: Trading Strategy Development - Explain the development of the trading strategy based on the intraday market data. Explain the papers you are using.

Slide 7: Backtesting - Discuss how the trading strategy was backtested on simulated (or historical) data to evaluate its performance.

Slide 8: Performance Metrics - Present the performance metrics used to evaluate the trading strategy, including Sharpe ratio, maximum drawdown, and win-loss ratio.

Slide 9: Sensitivity Analysis - Explain the sensitivity analysis performed to determine the robustness of the trading strategy to changes in parameters and assumptions.

Slide 10: Optimization - Describe the optimization process used to determine the optimal parameters and trading rules for the strategy.

Slide 11: Results - Present the results of the evaluation, including the performance metrics, sensitivity analysis, and optimization results.

Slide 12: Comparison with Existing Strategies - Compare the performance of the developed strategy with existing intraday trading strategies.

Slide 13: Conclusion and Limitations - Summarize the findings of the project, discuss the limitations of the study, and provide suggestions for future research.

Slide 14: Implementation - Discuss the potential implementation of the trading strategy in real-world trading scenarios.

Slide 15: References - List the references used in the project, including academic papers, books, and websites.

In this section, you will upload your presentation (pptx or google presentation or pdf)

