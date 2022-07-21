create table twm_checking_acct
(
    cust_id          INTEGER
        references twm_customer,
    acct_nbr         INTEGER
        constraint twm_checking_acct_pk
            primary key
        references twm_accounts,
    minimum_balance  INTEGER,
    per_check_fee    REAL,
    account_active   TEXT,
    acct_start_date  TEXT,
    acct_end_date    TEXT,
    starting_balance REAL,
    ending_balance   REAL
);

