from pandas.core.indexes import period
import yfinance as yf

stocks = yf.Ticker("GOOG")

stocks_data = stocks.history(period = "max")

print(stocks_data)