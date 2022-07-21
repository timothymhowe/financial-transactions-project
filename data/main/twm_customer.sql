create table twm_customer
(
    cust_id         INTEGER
        constraint twm_customer_pk
            primary key,
    income          INTEGER,
    age             INTEGER,
    years_with_bank INTEGER,
    nbr_children    INTEGER,
    gender          TEXT,
    marital_status  INTEGER,
    name_prefix     TEXT,
    first_name      TEXT,
    last_name       TEXT,
    street_nbr      INTEGER,
    street_name     TEXT,
    postal_code     INTEGER,
    city_name       TEXT,
    state_code      TEXT
);

