import numpy as np

def market_data(start_time, end_time, freq, time_dist="normal", price_dist="normal", qty_dist="normal"):
    curr_time = start_time
    prev_price = 100.0  # starting price

    while curr_time < end_time:
        # Generate time
        if time_dist == "normal":
            delta = np.random.normal(scale=freq.total_seconds(), size=None)
        elif time_dist == "lognormal":
            delta = np.random.lognormal(sigma=freq.total_seconds(), size=None)
        elif time_dist == "t":
            delta = np.random.standard_t(df=3, size=None) * freq.total_seconds()
        elif time_dist == "poisson":
            delta = np.random.poisson(lam=freq.total_seconds(), size=None)
        else:
            raise ValueError("Invalid time distribution")

        # Convert delta to timedelta64 and add to curr_time
        delta = np.timedelta64(int(delta), 'us')
        curr_time = np.datetime64(curr_time) + delta

        # Generate price increment using random walk
        if price_dist == "normal":
            increment = np.random.normal(loc=0, scale=0.001)
        elif price_dist == "lognormal":
            increment = np.random.lognormal(mean=0, sigma=0.001)
        elif price_dist == "t":
            increment = np.random.standard_t(df=3) * 0.001
        else:
            raise ValueError("Invalid price distribution")
        prev_price += increment

        # Generate bid and offer prices using the price increment and round them to 2 decimal places
        bid_price = round(prev_price - np.random.uniform(0.01, 0.10), 2)
        offer_price = round(bid_price + np.random.uniform(0.01, 0.10), 2)

        # Generate bid and offer quantities
        if qty_dist == "normal":
            bid_qty = np.random.normal(loc=1000, scale=100)
        elif qty_dist == "lognormal":
            bid_qty = np.random.lognormal(mean=1000, sigma=0.5)
        elif qty_dist == "poisson":
            bid_qty = np.random.poisson(lam=1000)
        else:
            raise ValueError("Invalid quantity distribution")
        offer_qty = bid_qty + np.random.randint(1, 10)

        # Yield market data
        yield (curr_time, bid_price, offer_price, bid_qty, offer_qty)



import datetime as dt

start_time = dt.datetime(2022, 1, 3, 9, 30, 0)
end_time = dt.datetime(2022, 1, 3, 16, 0, 0)
freq = dt.timedelta(milliseconds=1)

for data in market_data(start_time, end_time, freq, time_dist="poisson", price_dist="normal", qty_dist="poisson"):
    print(data)

