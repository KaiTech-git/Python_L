import os
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta
import csv
from get_all_tickers import get_tickers as gt
import sys


class Error(Exception):
    """Base class for other exceptions"""
    pass


class CompanyError(Error):
    """Raised when there is no such company Ticker in the base"""
    pass


# Create folder
c_dir = os.getcwd()
if os.path.isdir(c_dir + '/Downloaded'):
    pass
else:
    os.mkdir(c_dir + '/Downloaded')
if os.path.isdir(c_dir + '/Change'):
    pass
else:
    os.mkdir(c_dir + '/Change')
print(c_dir)
# Chose what companies to download
Tickers = [str(input('Give Ticker of a company which historical data you want to download (If done write ex):'))]
while Tickers[-1] != 'ex':
    Tickers.append(str(input('Give Ticker of a company which historical data you want to download (If done write ex):')))
Tickers.remove('ex')
Tickers=[x.upper() for x in Tickers] # make all strings consist of upper cases
try:
    list_of_tickers = gt.get_tickers()
    if not all(elem in list_of_tickers for elem in Tickers):
        raise CompanyError
except CompanyError:
    print('there is no such company Ticker in the base')
    sys.exit(1)
# Export data to CSV
today = date.today()
for Tk in Tickers:
    data_df = yf.download(Tk, start=str(today - relativedelta(years=1)), end=str(today))
    data_df.to_csv(c_dir + '/Downloaded/' + Tk + '.csv')  # New download overwrites old one

# Create change file
for Tkc in Tickers:
    with open(c_dir + '/Downloaded/' + Tkc + '.csv', 'r') as csv_unchanged:
        read = csv.DictReader(csv_unchanged)
        column_name = read.fieldnames
        column_name.append('Change')

        with open(c_dir + '/Change/' + Tkc + '.csv', 'w', newline='') as csv_change:
            writer = csv.DictWriter(csv_change, fieldnames=column_name)
            writer.writeheader()
            for row in read:
                change = (float(row['Close']) - float(row['Open'])) / float(row['Open'])
                row.update({'Change': change})
                writer.writerow(row)
