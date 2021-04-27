"""
Mock Biz process 2
------------------
Get the movers from the allquotes table and start a separate
getCandles for the candles table for just those stocks

Note
----
The first two biz processes can currently successfully share
the finnhub 300 calls per minute. We could probably speed those
up though

User Paramaters -- These should be provided by the user in a web app
--------------------------------------------------------------------
start
numrec
"""
import datetime as dt
import time
from quotedb.getdata import startCandles
from quotedb.getdata import getJustGainersLosers
from quotedb.utils import util
from quotedb import sp500
from quotedb.models.allquotes_candlemodel import AllquotesModel
from quotedb.models.candlesmodel import CandlesModel

stocks = sp500.getSymbols()
start =  util.dt2unix_ny(dt.datetime(2021, 4, 26, 9, 30))
end = util.dt2unix(dt.datetime.utcnow())
model = AllquotesModel
numrec = 50
local = True

glstocks = getJustGainersLosers(start, end, stocks, numrec, model, local)
startCandles(glstocks, start, CandlesModel, latest=True)
print(start)
print(len(stocks))