### Nossa Estratégia utilizando RNN forecast nos preços de 10 ativos selecionados
# usando forecast com Prophet e backtesting com fastquant

from fastquant import get_crypto_data, backtest
from fbprophet import Prophet
from matplotlib import pyplot as plt
