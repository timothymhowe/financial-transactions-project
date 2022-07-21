import pandas as pd
import numpy as np


twm_accounts = pd.read_csv('data/raw/twm_accounts.csv', delimiter=';')
twm_customer = pd.read_csv('data/raw/twm_customer.csv', delimiter=';')
twm_transactions = pd.read_csv('data/raw/twm_transactions.csv', delimiter=';')
twm_checking_acct = pd.read_csv('data/raw/twm_checking_acct.csv', delimiter=';')
twm_checking_tran = pd.read_csv('data/raw/twm_checking_tran.csv', delimiter=';')
twm_credit_acct = pd.read_csv('data/raw/twm_credit_acct.csv', delimiter=';')
twm_credit_tran = pd.read_csv('data/raw/twm_credit_tran.csv', delimiter=';')
twm_savings_acct = pd.read_csv('data/raw/twm_savings_acct.csv', delimiter=';')
twm_savings_tran = pd.read_csv('data/raw/twm_savings_tran.csv', delimiter=';')

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


def strip_all_columns(df):
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    return df


#%%
strip_all_columns(twm_customer).to_csv('data/clean/twm_customer.csv', sep=',', index=False)
strip_all_columns(twm_accounts).to_csv('data/clean/twm_accounts.csv', sep=',',index=False)
strip_all_columns(twm_transactions).to_csv('data/clean/twm_transactions.csv', sep=',',index=False)
strip_all_columns(twm_checking_acct).to_csv('data/clean/twm_checking_acct.csv', sep=',',index=False)
strip_all_columns(twm_checking_tran).to_csv('data/clean/twm_checking_tran.csv', sep=',', index=False)
strip_all_columns(twm_credit_acct).to_csv('data/clean/twm_credit_acct.csv', sep=',', index=False)
strip_all_columns(twm_credit_tran).to_csv('data/clean/twm_credit_tran.csv', sep=',', index=False)
strip_all_columns(twm_savings_acct).to_csv('data/clean/twm_savings_acct.csv', sep=',', index=False)
strip_all_columns(twm_savings_tran).to_csv('data/clean/twm_savings_tran.csv', sep=',', index=False)
