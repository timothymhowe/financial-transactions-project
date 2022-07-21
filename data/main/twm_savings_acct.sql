create table twm_savings_acct
(
    cust_id          INTEGER
        references twm_customer,
    acct_nbr         INTEGER
        constraint twm_savings_acct_pk
            primary key
        references twm_accounts,
    minimum_balance  INTEGER,
    acct_type        TEXT,
    account_active   TEXT,
    acct_start_date  TEXT,
    acct_end_date    TEXT,
    starting_balance REAL,
    ending_balance   REAL
);

