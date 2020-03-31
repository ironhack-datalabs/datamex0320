#update 1 value in existing data
# 1.- In invoices the value 201598 from 20001

SET SQL_SAFE_UPDATES = 0;
UPDATE invoices SET customer = 20001 WHERE id = 0;
select * from invoices
