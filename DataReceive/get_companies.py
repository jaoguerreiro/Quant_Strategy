###  OBJETIVO  ###
# Conseguir dados das top 10 empresas (critério: market cap) presentes no S&P500 por ano, a partir de 2010
# maior market cap tende a indicar empresas com situação financeira mais estável, 
# crescimento mais previsível e informações públicas completas.
# Um vez adquirida esta lista, importar o dados de preço e volume pelo yahoo


import yfinance as yf
import pandas as pd
from pandas_datareader import data


### OBTENDO DADOS DE 2021 pelo wikipedia
payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
first_table = payload[0]
second_table = payload[1]
df = first_table
df.drop(['Security', 'SEC filings', 'GICS Sub-Industry', 'Headquarters Location','Date first added', 'Founded'], axis='columns', inplace=True)
df.rename(columns = {'CIK':'Market Cap'}, inplace = True)

#Adicionando Market Cap ao DataFrame para filtrar as top 10.
#Obs: a consulta de get_quote_yahoo demora alguns minutos.
tickers = df['Symbol'].values.tolist()  
for ticker in tickers:
    if (("." not in ticker) & (ticker!='OGN')): ## remoção dos casos de erro em get_quote_yahoo (ausencia de dados)
        MarketCap = data.get_quote_yahoo(ticker)['marketCap']
        df.loc[df['Symbol'] == ticker, 'Market Cap'] = MarketCap[0]  #replace in the dataframe
    else: df.loc[df['Symbol'] == ticker, 'Market Cap'] = 0  #replace in the dataframe

df_top10 = df.nlargest(10, 'Market Cap')


### Salvando para CSV = ###
#df.to_csv('SP500MarketCap2021.csv', index = False)
#df_top10.to_csv('Top10MarketCap2021.csv', index = False)

print(df)
print(df_top10)

