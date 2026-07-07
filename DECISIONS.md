# Decisions

## v0.1 - Data Pipeline 

## Idempotent ingestion
Before the fix, running the loader twice duplicated every row (21 became 42). Now, before inserting each row, the code checks whether a row with the same ticker and date already exists, and skips it if so. Verified by wiping the table and running the loader twice: 21 rows after both runs. 

## Check-before-insert vs unique constraint
The stronger alternative is a unique constraint on (ticker, trade_date) in the database itself, because it refuses duplicates no matter what code writes to it, not just our one function. We chose the in-code check for v0. because it's simpler and good enough at this sacle. 