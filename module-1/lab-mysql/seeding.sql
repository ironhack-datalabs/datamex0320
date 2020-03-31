{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf610
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww17120\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\
insert into Cars (ID,VIN,Manufacturer,Model,Year,Color) values\
(0,'3K096I98581DHSNUP','Volkswagen','Tiguan','2019','Blue');\
insert into Cars (ID,VIN,Manufacturer,Model,Year,Color) values\
(1,'ZM8G7BEUQZ97IH46V','Peugeot','Rifter','2019','Red');\
insert into Cars (ID,VIN,Manufacturer,Model,Year,Color) values\
(2,'RKXVNNIHLVVZOUB4M','Ford','Fusion','2018','White');\
insert into Cars (ID,VIN,Manufacturer,Model,Year,Color) values\
(3,'HKNDGS7CU31E9Z7JW','Toyota','RAV4','2018','Silver');\
insert into Cars (ID,VIN,Manufacturer,Model,Year,Color) values\
(4,'DAM41UDN3CHU2WVF6','Volvo','V60','2019','Gray');\
insert into Cars (ID,VIN,Manufacturer,Model,Year,Color) values\
(5,'DAM41UDN3CHU2WVF6','Volvo','V60 Cross Country','2019','Gray');\
\
\
\
insert into Customers (ID,CustomerID,Name,Phone,Email,Adress,City,State,Country,Postal) values\
(0,'10001','Jose Juan','345678678','Juan@ironhack.com','Serafin Olarte 191','CDMX','CDMX','M\'e9xico','03630');\
insert into Customers (ID,CustomerID,Name,Phone,Email,Adress,City,State,Country,Postal) values\
(1,'10002','Argelia Anai','09876576','Anai@ironhack.com','San Borja 45','Cuernavaca','Morelos','M\'e9xico','86532');\
insert into Customers (ID,CustomerID,Name,Phone,Email,Adress,City,State,Country,Postal) values\
(2,'10003','Diana Belen','568734580','Belen@ironhack.com','Moctezuma 754','Los Angeles','California','EUA','07854');\
\
\
\
Insert into Salespersons (ID,StaffID,name,Store) values\
('0','00001','Petey Cruiser','Madrid'),\
(1,'00002','Anna Sthesia','Barcelona'),\
(2,'00003','Paul Molive','Berlin'),\
(3,'00004','Gail Forcewind','Paris'),\
(4,'00005','Paige Turner','Mimia'),\
(5,'00006','Bob Frapples','CDMX'),\
(6,'00007','Walter Melon','Amsterdam'),\
(7,'00008','Shonda Leer','S\'e3o Paulo');\
\
\
\
Insert into Invoices (ID,InvoiceNumber,Date,Car,Customer,SalesPerson) values\
('0','852399038','2018-08-22','0','1','3'),\
('1','731166526','2018-12-31','3','0','5'),\
('2','271135104','2018-01-22','2','2','7');\
\
\
\
\
}