import yfinance as yf

aapl = yf.Ticker("aapl")
aapl_historical = aapl.history(start="2023-02-05", end="2023-02-11", interval="1m")
aapl_historical
aapl.actions
data = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30")
