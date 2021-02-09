import csv
from datetime import datetime
from dateutil.parser import parse


path = "January_2021.csv"
file = open(path, newline='')
reader = csv.reader(file, delimiter = ',')

header = next(reader) # First line 
#test_data = [row for row in reader]

data = []
for row in reader:
    #row = ['Posted Account', ' Posted Transactions Date', ' Description1', ' Description2', ' Description3', ' Debit Amount', ' Credit Amount', 'Balance', 'Posted Currency', 'Transaction Type', 'Local Currency Amount', 'Local Currency']
    
    date_transaction = datetime.strptime(row[1], "%d/%m/%Y") # Convert str in Date type
    name_transaction = str(row[2]) # Convert in a STR
    value_transaction = float(row[10]) # Convert STR in Float type
    actual_balance_transaction = float(row[7]) # Convert STR in Float type
    posted_currency_transaction = str(row[8]) # Convert STR in Float type

    data.append([date_transaction,name_transaction,value_transaction, actual_balance_transaction,posted_currency_transaction])

print (data[1])
