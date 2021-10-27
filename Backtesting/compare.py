### Aqui geramos os resultados com estratégias básicas no mesmo período e mesmas acões
# para obter uma noção de desempenho da nossa estratégia com RNN

# Compara mavg, rsi e bbands com nossa estrategia

from fastquant import backtest, get_stock_data
import pandas as pd


df = pd.read_csv("DataReceive/2021Data/Top10MarketCap2021.csv")

tickers = df['Symbol'].values.tolist() 

final_values_mavg = []
final_values_rsi = []
final_values_bbands = []

for ticker in tickers:

    # Selecione aqui a data desejada (mesma que utilizada no backtest da estratégia)
    df = get_stock_data(ticker, "2010-01-01", "2015-01-01")
    df.drop(['open', 'high', 'low'], axis='columns', inplace=True)
    res = backtest('smac', df, fast_period=15, slow_period=40, plot = False)
    final_values_mavg.append(res['final_value'])
    res = backtest('rsi', df, rsi_period=14, rsi_upper=70, rsi_lower=30, plot = False)
    final_values_rsi.append(res['final_value'])
    res = backtest('bbands', df, period=20, devfactor=1.5, plot = False)
    final_values_bbands.append(res['final_value'])

# Resultados das estratégias:
print(final_values_mavg)
print(final_values_rsi)
print(final_values_bbands)


