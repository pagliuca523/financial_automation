import pandas as pd

#print (import_db_path[[" Posted Transactions Date", " Description1", "Transaction Type", "Local Currency Amount", "Posted Currency" ]])
#filter_data = new_import_db.loc[import_db_path[" Description1"].str.contains("MCDONAL")]

import_db_path = pd.read_csv("January_2021.csv", na_values = ['no info', '.'])
new_import_db = import_db_path[[" Posted Transactions Date", " Description1", "Transaction Type", "Local Currency Amount", "Posted Currency" ]]

#Create Month Column
def create_month_column():
    #months = ("January","February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    new_import_db["Month"] = new_import_db[" Posted Transactions Date"].str[3:5]
    new_import_db["Month"] = new_import_db["Month"].astype("int")

#Sum based month

def sum_monthly():
    
    total_sum_monthly = new_import_db.groupby("Month").sum()
    total_sum_transactions = new_import_db.groupby("Transaction Type").sum()
    print(total_sum_transactions)

def locate_debit():
    locate_debit_results = new_import_db.loc[lambda row: row["Transaction Type"].str.startswith("D")]
    #loc_desc = locate_debit_results.describe() #Count, Min, Avg values
    #results = locate_debit_results.groupby(" Description1").sum()
    print(locate_debit_results)
    #print (results)

def locate_credit():
    locate_credit_results = new_import_db.loc[lambda row: row["Transaction Type"].str.startswith("C")]
    print(locate_credit_results)

def create_labels():
    
    pass

    

create_month_column()
sum_monthly()
locate_debit()
locate_credit()
create_labels()
#print(new_import_db)
