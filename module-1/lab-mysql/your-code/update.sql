#updating Miami

UPDATE sales_persons
SET store_name = "Miami"
WHERE id=4;


#updating emails in customer table

UPDATE Customer
SET email = "ppicasso@gmail.com"
WHERE customer_name = "Pablo Picasso";

UPDATE Customer
SET email = "lincoln@us.gov"
WHERE customer_name = "Abraham Lincoln";

UPDATE Customer
SET email = "hello@napoleon.me"
WHERE customer_name = "Napoléon Bonaparte";

