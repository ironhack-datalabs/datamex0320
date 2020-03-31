update customers set last_name='Zambada'
where first_name='Chapo';

ALTER TABLE customers
ADD email varchar(50) NOT NULL
AFTER last_name;

INSERT INTO customers (email)
VALUES ('mjordan@airjordan.com'),
		('czambada@gmail.com');

