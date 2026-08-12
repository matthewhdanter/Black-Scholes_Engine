# Matthew Danter - Black-Scholes Engine
import numpy as np
from scipy.stats import norm
import pandas as pd

# Below are the parameters set by the user:
# The name of the price history file, as a string:
HistoryFile = "example1.csv"

# The name of the options chain file, as a string:
OptionsFile = "example2.csv"

# The risk-free interest rate:
rfir = .045


# First I will write the function:

def MD_BSE(spot, strike, tmat, rfir, vol):
    # The function will perform the Black-Scholes model to price European Options
    # Another project for later could be to execute the model using an FDM to price American Options
    # spot --> Spot Price: current market price of asset
    # strike --> Strike Price: price specified on contract
    # tmat --> Time to Maturity: time remaining until the contract expires
    # rfir --> Risk-Free Interest Rate: theoretical return of a zero-risk investment
    # vol --> Volatility: speed and size of a stock's price swings

    # First find d1 and d2 which will be converted to probabilities
    d1 = (np.log(spot/strike) + (rfir + (vol ** 2)/2) * tmat)/(vol * np.sqrt(tmat))
    d2 = d1 - vol*np.sqrt(tmat)

    # Convert to probabilities, N(d1) accounts for risk and N(d2) is the probability of expiring in the money
    Nd2 = norm.cdf(d2)
    Nd1 = norm.cdf(d1)

    # Perform closed form Black-Scholes to determine Call Price
    call = spot * Nd1 - strike * np.exp(-rfir * tmat) * Nd2

    # Use Put-Call Parity to find Put option price:
    put = call + strike * np.exp(-rfir * tmat) - spot
    return call, put

# Now I will write the code to parse through the data and pull out the needed values:
# Two files need to be parsed:
# File one is the history of the option:
history = pd.read_csv(HistoryFile)

# From this file I will get the spot price and the volatility:
# Spot price, the final closing price:
spot = history['Close'].iloc[-1]

# The volatility is the standard deviation of the column 'Close'
vol = (history["Close"].pct_change().std()) * np.sqrt(252)

# File two has all available options presently
options = pd.read_csv(OptionsFile, parse_dates = ["Expiration"])

# From this file, get the strike price and time to maturity, and append the call and put prices:
for row in options.itertuples():
    # Strike price:
    strike = row.Strike
   
    # Time to maturity
    # Expiration date:
    expiration = row.Expiration

    # Subtract today's date with expiration date and annualize:
    tmat = ((expiration - pd.Timestamp('today').normalize()).total_seconds())/(86400*365)

    # Now all of the parameters have been obtained and the engine can be run:
    call, put = MD_BSE(spot, strike, tmat, rfir, vol)

    # Append:
    options.loc[row.Index,"Call"] = call
    options.loc[row.Index,"Put"] = put

# Finally, write everything to a new CSV File:
options.to_csv("Output1.csv")