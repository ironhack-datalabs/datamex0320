CREATE TABLE `lab_mysql`.`Cars` (
  `VIN` VARCHAR(45) NOT NULL,
  `Manufacturer` VARCHAR(45) NULL,
  `Model` VARCHAR(45)NULL,
  `Year` VARCHAR(45)NULL,
  `Color` VARCHAR(45)NULL,
  PRIMARY KEY (`VIN`));
  

CREATE TABLE `lab_mysql`.`Customer` (
  `Customer_ID` INT NOT NULL,
  `Name` VARCHAR(45)NULL,
  `Phone` VARCHAR(45)NULL,
  `Email` VARCHAR(45)NULL,
  `Address` VARCHAR(45)NULL,
  `City` VARCHAR(45)NULL,
  `State/Province` VARCHAR(45)NULL,
  `Country` VARCHAR(45)NULL,
  `Zip/Postal code` VARCHAR(45)NULL,
  PRIMARY KEY (`Customer_ID`));
  

CREATE TABLE `lab_mysql`.`Salespersons` (
  `Staff ID` INT NOT NULL,
  `Name` VARCHAR(45)NULL,
  `Store` VARCHAR(45)NULL,
  PRIMARY KEY (`Staff ID"));


CREATE TABLE `lab_mysql`.`Invoices` (
  `Invoice Number` INT NOT NULL,
  `Date` DATE NULL,
  `Car` VARCHAR(45)NULL,
  `Customer` VARCHAR(45)NULL,
  `Sales Person` VARCHAR(45)NULL,
  PRIMARY KEY (`Invoice Number`));

