"""
Mock Biz process 1 
------------------
should run from open to close to keep AllQuotes table
up to date

User paramaters -- Should be provide by the user in a web app
-------------------------------------------------------------
start
"""
import datetime as dt
from quotedb.getdata import startCandles
from quotedb.utils import util
from quotedb import sp500
from quotedb.models.allquotes_candlemodel import AllquotesModel

stocks = sp500.getSymbols()
start =  util.dt2unix_ny(dt.datetime(2021, 4, 26, 9, 30))
model = AllquotesModel

startCandles(stocks, start, model, latest=True)