import numpy as np
import pandas as pd


def market_data(start_time, end_time, dt, mean_time, mean_bid, mean_offer, bid_qty, offer_qty, volatility):
    """
    Generates intraday market data with a timestamp, bid price, bid quantity, offer price, and offer quantity.
    """
    # Initialize empty lists to store the data
    timestamps = []
    bid_prices = []
    bid_quantities = []
    offer_prices = []
    offer_quantities = []

    # Initialize the starting prices
    bid_price = np.random.normal(mean_bid, volatility)
    offer_price = np.random.normal(mean_offer, volatility)

    # Set the initial timestamp
    timestamp = start_time

    # Loop through each time step
    while timestamp < end_time:
        # Append the current timestamp to the list
        timestamps.append(timestamp)

        # Generate a new bid price and offer price using a random walk process
        bid_price += np.random.normal(0, volatility)
        offer_price += np.random.normal(0, volatility)

        # Ensure the bid price is always lower than the offer price
        if bid_price >= offer_price:
            bid_price = offer_price - 0.01

        # Append the bid and offer prices to the list
        bid_prices.append(round(bid_price, 2))
        offer_prices.append(round(offer_price, 2))

        # Generate a new bid quantity and offer quantity using a Poisson process
        bid_quantity = np.random.poisson(bid_qty)
        offer_quantity = np.random.poisson(offer_qty)

        # Append the bid and offer quantities to the list
        bid_quantities.append(bid_quantity)
        offer_quantities.append(offer_quantity)

        # Generate the next timestamp using a Poisson process
        dt = np.random.exponential(scale=mean_time)
        timestamp += pd.Timedelta(dt, unit='us')

    # Return the data as a Pandas DataFrame
    return pd.DataFrame({
        'Timestamp': timestamps,
        'Bid Price': bid_prices,
        'Bid Quantity': bid_quantities,
        'Offer Price': offer_prices,
        'Offer Quantity': offer_quantities
    })


start_time = pd.Timestamp('2023-03-03 09:00:00')
end_time = pd.Timestamp('2023-03-03 16:30:00')
# microseconds
dt = pd.Timedelta(1, unit='us')
mean_time = 1e6
mean_bid = 100
mean_offer = 101
bid_qty = 1000
offer_qty = 1000
volatility = 0.01


print(market_data(start_time, end_time, dt, mean_time, mean_bid, mean_offer, bid_qty, offer_qty, volatility))
