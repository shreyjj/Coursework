import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import csv

my_share = share.Share('^FTSE')
symbol_data = None
f = csv.writer(open('data-from-ftse.txt', 'w'))
f.writerow(['Data'])

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                          5,
                                          share.FREQUENCY_TYPE_MINUTE,
                                          60)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)


f.writerow([symbol_data])

times = symbol_data['timestamp']
open = symbol_data['open']
close = symbol_data['close']
for i in range(20):
    print(times[i], "\t", open[i])

