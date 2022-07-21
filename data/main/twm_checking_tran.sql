create table twm_checking_tran
(
    cust_id       INTEGER
        references twm_customer,
    tran_id       INTEGER,
    tran_amt      REAL,
    principal_amt REAL,
    interest_amt  REAL,
    new_balance   REAL,
    tran_date     TEXT,
    tran_time     INTEGER,
    channel       TEXT,
    tran_code     TEXT,
    constraint twm_checking_tran_pk
        primary key (cust_id, tran_id)
);

