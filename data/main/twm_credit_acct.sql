create table twm_credit_acct
(
    cust_id          INTEGER
        references twm_customer,
    acct_nbr         REAL
        constraint twm_credit_acct_pk
            primary key
        references twm_accounts,
    credit_limit     INTEGER,
    credit_rating    INTEGER,
    account_active   TEXT,
    acct_start_date  TEXT,
    acct_end_date    TEXT,
    starting_balance REAL,
    ending_balance   REAL
);

