USE lab_mysql;

Tabla cars

CREATE TABLE `lab_mysql`.`cars` (
  `id_cars` VARCHAR(45) NOT NULL,
  `vin` VARCHAR(45) NOT NULL,
  `manufacture` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` YEAR(4) NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_cars`));


Tabla customer
Executing:
CREATE TABLE `lab_mysql`.`customers` (
  `Idnum` INT NOT NULL,
  `id_customer` VARCHAR(45) CHARACTER SET 'ascii' NOT NULL,
  `name` TEXT(45) NOT NULL,
  `phone` INT NOT NULL,
  `email` VARCHAR(45) NULL,
  `adress` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state_province` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `postal` INT NOT NULL,
  PRIMARY KEY (`id_customer`));

tabla salespersons 

CREATE TABLE `lab_mysql`.`salespersons` (
  `id_num` INT NOT NULL,
  `id_staff` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_staff`));


 tabla invoices

CREATE TABLE `lab_mysql`.`invoices` (
  `id_numin` INT NOT NULL,
  `invoice_number` VARCHAR(45) NOT NULL,
  `date` VARCHAR(45) NOT NULL,
  `car` VARCHAR(45) NOT NULL,
  `customer` VARCHAR(45) NOT NULL,
  `salesperson` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`invoice_number`));