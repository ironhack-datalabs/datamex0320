insert into cars (id, VIN, Manufacturer, Model, Year, Color) 
values ('0', '3K096I98581DHSNUP', 'Volkswagen','Tiguan','2019','Blue');

insert into cars (id, VIN, Manufacturer, Model, Year, Color) 
values ('1', 'ZM8G7BEUQZ97IH46V', 'Peugeot','Rifter','2019','Red');

insert into cars (id, VIN, Manufacturer, Model, Year, Color) 
values ('2', 'RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', '2018', 'White');

insert into cars (id, VIN, Manufacturer, Model, Year, Color) 
values ('3', 'HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', '2018', 'Silver');

select * from cars;

insert into customer (id, insuranceid, brand, phone, email, Addres) 
values ('0', '20001', 'Aguila','55487923','aguila25@ag.com','Polanco');

insert into customer (id, insuranceid, brand, phone, email, Addres) 
values ('1', '20054', 'Qualitas','55849923','Qualitas56@Qlt.com','Roma Norte');

insert into customer (id, insuranceid, brand, phone, email, Addres) 
values ('2', '20048', 'Bancomer','55841233','Bancomer56@Banc.com','Lindavista');

insert into customer (id, insuranceid, brand, phone, email, Addres) 
values ('3', '20016', 'OEM´s','55841233','Bancomer56@Banc.com','Ajusco');

select * from customer;

insert into salespersons (id, staff_id, name) 
values ('0', '201598', 'Juan R');

insert into salespersons (id, staff_id, name) 
values ('1', '201556', 'Raul S');

insert into salespersons (id, staff_id, name) 
values ('2', '201512', 'Pedro O');

insert into salespersons (id, staff_id, name) 
values ('3', '201532', 'Rosalia T');

select * from salespersons;

insert into invoices (id, invoice_number, VIN, customer, salesperson) 
values ('0', '48956318', '3K096I98581DHSNUP', '201598', '201598');

insert into invoices (id, invoice_number, VIN, customer, salesperson) 
values ('1', '48956319', 'ZM8G7BEUQZ97IH46V', '20054', '201556');

insert into invoices (id, invoice_number, VIN, customer, salesperson) 
values ('2', '48956320', 'RKXVNNIHLVVZOUB4M', '20048', '201512');

insert into invoices (id, invoice_number, VIN, customer, salesperson) 
values ('3', '48956321', 'HKNDGS7CU31E9Z7JW', '20016', '201532');

select * from invoices;