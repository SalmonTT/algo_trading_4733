# algo_trading_4733
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

However, we can also use [TrueFX](https://www.truefx.com/) to obtain tick data of currency pairs. 

## Stage 2: Create Bar Data
You will create bar data and you will explain the different kind of bar data you managed to create.  
Types of bar data:
- time bars

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

