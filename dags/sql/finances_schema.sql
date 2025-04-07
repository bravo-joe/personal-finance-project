-- Beginning of "finances_schema.sql"
/*
Create the table schema for the personal finances project.
NB: Each month will have its own table.
txn <-- abbreviation for transaction.
txn_id will be serial primary key and be first column.
*/
CREATE TABLE IF NOT EXISTS dec_2023 (
    txn_id SERIAL PRIMARY key
    , date DATE NOT NULL
    , day VARCHAR NOT NULL
    , description VARCHAR NOT NULL
    , category VARCHAR NOT NULL
    , amount VARCHAR NOT NULL
);
-- End of "finances_schema.sql"
