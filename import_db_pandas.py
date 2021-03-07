import pandas as pd
import dict_months as d_months

#print (import_db_path[[" Posted Transactions Date", " Description1", "Transaction Type", "Local Currency Amount", "Posted Currency" ]])
#filter_data = new_import_db.loc[import_db_path[" Description1"].str.contains("MCDONAL")]

# Asking user for the range of data to be used to run de application
user_month = int(input("Which MONTH would like to analyse (1-12)? "))
year_month = str(input("Which YEAR would like to analyse? "))

name_db_selection = str(d_months.months[user_month])+"_"+str(year_month)+".csv" #Converting data from inputs in a Standard names for files
print("You are analiysing data from: {}".format(name_db_selection))
import_db_path = pd.read_csv(name_db_selection, na_values = ['no info', '.'])
new_import_db = import_db_path[[" Posted Transactions Date", " Description1", "Transaction Type", "Local Currency Amount", "Posted Currency", "TYPE" ]]


#Create Month Column
def create_month_column():
    #months = ("January","February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    new_import_db["Month"] = new_import_db[" Posted Transactions Date"].str[3:5]
    new_import_db["Month"] = new_import_db["Month"].astype("int")

#Sum based month

def sum_monthly():
    
    #total_sum_monthly = new_import_db.groupby("Month").sum()
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

def sum_by_type_debit():
    total_sum_by_type_month = new_import_db[new_import_db["Month"] == user_month]
    total_sum_by_type_d = new_import_db[new_import_db["Transaction Type"] == "Debit"].groupby("TYPE").sum().sort_values(by='Local Currency Amount', ascending=False)
    print(total_sum_by_type_d)

def sum_by_type_credit():
    total_sum_by_type_month = new_import_db[new_import_db["Month"] == user_month]
    total_sum_by_type_d = new_import_db[new_import_db["Transaction Type"] == "Credit"].groupby("TYPE").sum().sort_values(by='Local Currency Amount', ascending=False)
    print(total_sum_by_type_d)
    

    

create_month_column()
sum_monthly()
locate_debit()
locate_credit()
sum_by_type_debit()
sum_by_type_credit()
#print(new_import_db)
