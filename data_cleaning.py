import pandas as pd
import numpy as np
from dateutil import parser
from datetime import datetime

twm_accounts = pd.read_csv('data/raw/twm_accounts.csv', delimiter=';')
twm_customer = pd.read_csv('data/raw/twm_customer.csv', delimiter=';', dayfirst=True, parse_dates=True)
twm_transactions = pd.read_csv('data/raw/twm_transactions.csv', delimiter=';', dayfirst=True, parse_dates=True)
twm_checking_acct = pd.read_csv('data/raw/twm_checking_acct.csv', delimiter=';', dayfirst=True, parse_dates=True)
twm_checking_tran = pd.read_csv('data/raw/twm_checking_tran.csv', delimiter=';', dayfirst=True, parse_dates=True)
twm_credit_acct = pd.read_csv('data/raw/twm_credit_acct.csv', delimiter=';', dayfirst=True, parse_dates=True)
twm_credit_tran = pd.read_csv('data/raw/twm_credit_tran.csv', delimiter=';', dayfirst=True, parse_dates=True)
twm_savings_acct = pd.read_csv('data/raw/twm_savings_acct.csv', delimiter=';', dayfirst=True, parse_dates=True)
twm_savings_tran = pd.read_csv('data/raw/twm_savings_tran.csv', delimiter=';', dayfirst=True, parse_dates=True)

twm_files = (twm_accounts,
             twm_transactions,
             twm_customer,
             twm_checking_acct,
             twm_checking_tran,
             twm_credit_tran,
             twm_credit_acct,
             twm_savings_tran,
             twm_savings_acct
             )

print
def strip_all_columns(df):
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    return df


def format_date_string(string):
    string = str(string)
    if '.' not in string:
        return None
    else:
        return str(datetime.date(parser.parse(string, dayfirst=True, fuzzy=True)))


def fix_dates(df, columns):

    for col in columns:
        df[col] = df[col].map(format_date_string)

def format_time_string(string):
    string = str(string)
    if len(string) < 4:
        return None
    elif len(string) < 6:
        string = "0" + string

    return str(datetime.time(datetime.strptime(string, "%H%M%S")))


def fix_time (df, columns):
    for col in columns:
        df[col] = df[col].map(format_time_string)


twm_customer = strip_all_columns(twm_customer)
twm_accounts = strip_all_columns(twm_accounts)
twm_transactions = strip_all_columns(twm_transactions)
twm_checking_acct = strip_all_columns(twm_checking_acct)
twm_checking_tran =strip_all_columns(twm_checking_tran)
twm_credit_acct = strip_all_columns(twm_credit_acct)
twm_credit_tran = strip_all_columns(twm_credit_tran)
twm_savings_acct = strip_all_columns(twm_savings_acct)
twm_savings_tran = strip_all_columns(twm_savings_tran)

fix_dates(twm_accounts, ['acct_start_date','acct_end_date'])
fix_dates(twm_checking_acct, ['acct_start_date','acct_end_date'])
fix_dates(twm_savings_acct, ['acct_start_date','acct_end_date'])
fix_dates(twm_credit_acct, ['acct_start_date','acct_end_date'])

fix_dates(twm_transactions,['tran_date'])
fix_dates(twm_savings_tran,['tran_date'])
fix_dates(twm_checking_tran,['tran_date'])
fix_dates(twm_credit_tran,['tran_date'])

fix_time(twm_transactions,['tran_time'])
fix_time(twm_savings_tran,['tran_time'])
fix_time(twm_checking_tran,['tran_time'])
fix_time(twm_credit_tran,['tran_time'])



# %%
twm_customer.to_csv('data/clean/twm_customer.csv', sep=',', index=False)
twm_accounts.to_csv('data/clean/twm_accounts.csv', sep=',', index=False)
twm_transactions.to_csv('data/clean/twm_transactions.csv', sep=',', index=False)
twm_checking_acct.to_csv('data/clean/twm_checking_acct.csv', sep=',', index=False)
twm_checking_tran.to_csv('data/clean/twm_checking_tran.csv', sep=',', index=False)
twm_credit_acct.to_csv('data/clean/twm_credit_acct.csv', sep=',', index=False)
twm_credit_tran.to_csv('data/clean/twm_credit_tran.csv', sep=',', index=False)
twm_savings_acct.to_csv('data/clean/twm_savings_acct.csv', sep=',', index=False)
twm_savings_tran.to_csv('data/clean/twm_savings_tran.csv', sep=',', index=False)

# %%
