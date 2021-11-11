### Nossa Estratégia utilizando RNN forecast nos preços de 10 ativos selecionados
# usando forecast com Prophet e backtesting com fastquant

from fastquant import get_crypto_data, backtest
from prophet import Prophet
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


### Selecionando Serie de Precos
companies = pd.read_csv("DataReceive/2021Data/Top10MarketCap2021.csv")
companies = companies['Symbol'].values.tolist() 
stocks = yf.Tickers( companies )
# Escolhendo período a ser coletado
stock_data_train = stocks.history(start = "2010-01-01", end = "2020-01-03")
stock_data_test = stocks.history(start = "2020-01-03", end = "2021-01-01")
# Escolhendo quais dados não serão usados 
stock_data_train.drop(['Stock Splits', 'Dividends', 'High', 'Low', 'Open', 'Volume'], axis='columns', inplace=True)
stock_data_test.drop(['Stock Splits', 'Dividends', 'High', 'Low', 'Open', 'Volume'], axis='columns', inplace=True)
#for ticker in companies:
ticker = companies[0]
dtf_train = stock_data_train['Close'][ticker]
dtf_test = stock_data_test['Close'][ticker]
# Fit model on closing prices
ts_train = dtf_train.reset_index()
ts_train.columns = ['ds', 'y']
ts_test = dtf_test.reset_index()
ts_test.columns = ['ds', 'y']


# Prediction on future data
model = Prophet().fit(ts_train)
forecast = model.make_future_dataframe(periods=365, freq='D', include_history=False )  

pred = model.predict(forecast)
print(pred)
next_day = pred['yhat'][0]

#Plotting
fig1 = model.plot(pred)
plt.plot(dtf_test)
plt.title('BTC/USDT: Forecasted Daily Closing Price', fontsize=25)
plt.show()

# Convert predictions to expected 1 day returns
expected_1day_return = pred.set_index("ds").yhat.pct_change().shift(-1).multiply(100)

# Backtest the predictions, given that we buy bitcoin when the predicted next day return is > +1.5%, and sell when it's < -1.5%.
dtf_test["custom"] = expected_1day_return.multiply(-1)
#backtest("custom", dtf_test.dropna(),upper_limit=1.5, lower_limit=-1.5)