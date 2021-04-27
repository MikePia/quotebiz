"""
Mock biz process 4

User Paramaters
---------------
fq can be a Firstquote type or a date (int unix time). It represents the baseline quote for deltas/accumulators
fn can be a regex  or simply the first part of the filename. 
    This is the name of the input file to match
    Quotedb will match the greatest alphanumeric match to the fn pattern and return the latest timestamp matched.
    Or it can be the entire name

Note
----
The current output filename is not a user option in version 1.0.7 of quotedb. It will be
visualize_out_{timestamp}.json
"""

import datetime as dt
from quotedb.getdata import visualizeData
from quotedb.utils import util

fq = util.dt2unix_ny(dt.datetime(2021, 4, 26, 3, 30))
fn = "^mockbiz"
vfn = visualizeData(fn, fq)
print(f'File is located {vfn}')