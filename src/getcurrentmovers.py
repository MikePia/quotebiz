"""
Mock Biz process 3
Get the movers from the candles table and subscribe those to the 
WebSocket

Note
----
This is real time only and needs to run when the market is open. The
only stocks in the result file are stocks that have trades in real time
now.
If Mock Biz Processes 1, 2, and 3 are all run simultaneosly, it will
likely cause a finnhub  MaxLimit failure and kick out of the websocket.


User Paramaters -- These should be provided by the user in a web app
--------------------------------------------------------------------
start
numstocks
fn
"""
import datetime as dt
import os

from quotedb.dbconnection import getCsvDirectory
from quotedb.getdata import startTickWSKeepAlive
from quotedb.models.candlesmodel import CandlesModel
from quotedb.models.managecandles import ManageCandles
from quotedb.utils import util

mc = ManageCandles(None, CandlesModel)
stocks = mc.getTickers()
start = util.dt2unix_ny(dt.datetime(2021, 4, 26, 3, 30))
numstocks = 12
gainers, losers = mc.filterGainersLosers(stocks, start, numstocks)
gainers.extend(losers[1:])
gainers = [x[0] for x in gainers][1:]
# This bogus addition of bitcoin allows it to run after hours and get something from the websocket server most any time 24/7
gainers.append('BINANCE:BTCUSDT')
print(len(gainers))

fn = util.formatFn("mockbiz.json", 'json')
fn
fn =os.path.normpath(fn)
startTickWSKeepAlive(gainers, fn, ['json'], delt=None, polltime=5)
