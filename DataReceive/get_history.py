### Obter para as empresas selecionadas as series de dados de preco e volume
#

import pandas as pd
import yfinance as yf

# Escolhendo que arquivo de empresas analizar
df = pd.read_csv("DataReceive/2021Data/Top10MarketCap2021.csv")

stocks_tickers = df['Symbol'].values.tolist() 

stocks = yf.Tickers( stocks_tickers )

    # Escolhendo período a ser coletado
stock_data = stocks.history(start = "2010-01-01", end = "2021-01-01")

    # Escolhendo quais dados não serão usados 
stock_data.drop(['Stock Splits', 'Dividends', 'High', 'Low', 'Open', 'Volume'], axis='columns', inplace=True)

for ticker in stocks_tickers:
    print(stock_data['Close'][ticker])

# Salvando em CSV
#stock_data.to_csv('DataReceive/2021Data/History_SelectedCompanies.csv')

# FIltrando dados de uma única empresas
#one_stock_data = pd.concat( [ stock_data['Close', 'AAPL'] , stock_data['Volume', 'AAPL'] ], axis=1 )
