create table twm_accounts
(
    acct_nbr         REAL
        constraint twm_accounts_pk
            primary key,
    cust_id          INTEGER
        references twm_customer,
    acct_type        TEXT,
    account_active   TEXT,
    acct_start_date  TEXT,
    acct_end_date    TEXT,
    starting_balance REAL,
    ending_balance   REAL
);

