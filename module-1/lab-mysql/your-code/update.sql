
#updating email for Picasso
UPDATE customer 
SET 
    email = 'ppicasso@gmail.com'
WHERE
    customer_id = 10001;

#updating email for Lincon
UPDATE customer 
SET 
    email = 'lincoln@us.gov'
WHERE
    customer_id = 20001;

#updating email for Napoleon
UPDATE customer 
SET 
    email = 'hello@napoleon.me'
WHERE
    customer_id = 30001;


#correcting store value for Paige Turner

UPDATE salespersons
SET 
    store = 'Miami'
WHERE
    staff_id = 00005;