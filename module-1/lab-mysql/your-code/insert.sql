# Values fro the cars table 

INSERT INTO cars (car_id, manufacturer, model, year, color, price)
	VALUES (529180, 'Lincoln', 'Aviator', 2020, 'Black', 51000), 
	(437142, 'Tesla', 'Model S', 2012, 'Black', 79900), 
	(632424, 'Cadillac', 'XT4', 2010, 'White', 38000), 
	(734738, 'Chevrolet', 'Spark', 2009, 'Orange', 25000), 
	(390652, 'GMC', 'Sierra 3500', 2020, 'Blue', 40800), 
	(404265, 'Chrysler', 'Chrysler Pacifica', 2017, 'White', 28600), 
	(882710, 'Dodge', 'Dodge Avenger', 2008, 'Gray', 19000), 
	(883325, 'Jeep', 'Grand Cherokee', 2015, 'White', 20000), 
	(368368, 'RAM', 'RAM 1500', 2014, 'Red', 15000), 
	(837409, 'Ford', 'Ford' 'Everest', 2019, 'Gray', 54500);


# Values fro the customers table

INSERT INTO customers (customer_id, name, phone, email, addres, city, state, country, postal_code, age)
VALUES (89755, 'Saniya Winters', '(200) 314-8999', '', '688 Monroe Ave.', 'Lockport', 'NY', 'US', 14094, 34),
	   (35349, 'Cassia Ferreira', '(475) 874-6900', '', '8081 Wayne St.', 'Newport News', 'VA', 'US', 23601, 55),
	   (00442, 'Gene Goddard', '(593) 272-1892', '', '8519 Hall Ave.', ' Olive Branch', 'MS', 'US', 38654, 42),
	   (07637, 'Ursula Walsh', '(968) 254-2310', '', '61 Bay Road West', ' Islip', 'NY', 'US', 11795, 28);


# Values fro the salespersons table

INSERT INTO salespersons (staff_id, name, store, age)
VALUES (28851, 'Remi Kirby', 'Islip', 25),
	   (64585, 'Adelina Hackett', 'Columbus', 45),
	   (64364, 'Haley Rivers', 'Newport News', 34),
	   (01517, 'Sohaib Dudley', 'Olive Branch', 29),
	   (25153, 'Sumaiya Hawes', 'Islip', 38),
	   (37996, 'Caitlin Irwin', 'Lockport', 32),
	   (18521, 'Reagan Mcgill', 'Newport News', 27),
	   (51403, 'Sammy Finch', 'Rochester', 46);


# Values fro the salespersons table

INSERT INTO invoices (invoice_number, date_in, car, customer, staff)
VALUES (947071, '2008-03-27', 882710, 89755, 37996),
	   (597028, '2008-10-22', 882710, 35349, 18521),
	   (286844, '2013-02-11', 437142, 07637, 25153),
	   (484978, '2014-09-29', 368368, 89755, 37996),
	   (444025, '2018-07-02', 883325, 00442, 01517);