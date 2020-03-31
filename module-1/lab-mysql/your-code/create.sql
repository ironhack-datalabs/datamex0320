# crear base de datos

CREATE DATABASE lab_mysql;

# usar base de datos

USE lab_mysql;

# crear tabla cars
CREATE TABLE `lab_mysql`.`Cars` (
  `VIN` VARCHAR(45) NOT NULL,
  `Manufactor` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` YEAR(4) NULL,
  `Color` VARCHAR(45) NULL,
  PRIMARY KEY (`VIN`));

# crear tabla customer
CREATE TABLE `lab_mysql`.`Customer` (
  `Customer_ID` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL DEFAULT '+',
  `Email` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `State` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `ZIP` INT NULL,
  PRIMARY KEY (`CustomerID`));

# crear tabla Salespersons
CREATE TABLE `lab_mysql`.`Salespersons` (
  `Staff_ID` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  PRIMARY KEY (`Staff ID`));

# crear tabla invoices
CREATE TABLE `lab_mysql`.`Invoices` (
  `Invoice_Number` INT NOT NULL,
  `Date` DATETIME NULL,
  `Car` INT NULL,
  `Customer` INT NULL,
  `Sales_Person` INT NULL,
  PRIMARY KEY (`Invoice Number`));



