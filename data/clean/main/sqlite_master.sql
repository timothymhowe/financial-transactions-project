alter table sqlite_master
    add type TEXT;

alter table sqlite_master
    add name TEXT;

alter table sqlite_master
    add tbl_name TEXT;

alter table sqlite_master
    add rootpage INT;

alter table sqlite_master
    add sql TEXT;

