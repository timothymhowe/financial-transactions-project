create table twm_transactions
(
    tran_id       INTEGER,
    acct_nbr      REAL
        references twm_accounts,
    tran_amt      REAL,
    principal_amt REAL,
    interest_amt  REAL,
    new_balance   REAL,
    tran_date     TEXT,
    tran_time     INTEGER,
    channel       TEXT,
    tran_code     TEXT,
    constraint twm_transactions_pk
        primary key (acct_nbr, tran_id)
);

