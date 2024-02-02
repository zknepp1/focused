CREATE TABLE `Photographers` (
  `PhotographerID` integer PRIMARY KEY,
  `JobID` integer,
  `photographerfname` varchar(255) NOT NULL,
  `photographerlname` varchar(255) NOT NULL,
  `photographerContactNumber` varchar(255),
  `photographerEmail` varchar(255)
);

CREATE TABLE `Customers` (
  `CustomerID` integer PRIMARY KEY,
  `customerfname` varchar(255) NOT NULL,
  `customerlname` varchar(255) NOT NULL,
  `customerContactNumber` varchar(255) NOT NULL,
  `customerEmail` varchar(255) NOT NULL,
  `customerAddress` varchar(255) NOT NULL
);

CREATE TABLE `Jobs` (
  `JobID` integer PRIMARY KEY,
  `SchoolName` varchar(255) NOT NULL,
  `pictureDate` timestamp NOT NULL,
  `schoolLocation` varchar(255) NOT NULL,
  `schoolContactNumber` varchar(255) NOT NULL,
  `schoolEmail` varchar(255) NOT NULL,
  `schoolAddress` varchar(255) NOT NULL
);

CREATE TABLE `Students` (
  `StudentID` integer PRIMARY KEY,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `teacher` varchar(255) NOT NULL,
  `GradeOrClass` varchar(255) NOT NULL,
  `barcodeID` integer NOT NULL,
  `JobID` integer
);

CREATE TABLE `PriceSheets` (
  `PriceSheetID` integer PRIMARY KEY,
  `ItemDescription` varchar(255),
  `Price` integer,
  `SizeOrFormat` integer,
  `Discount` integer
);

CREATE TABLE `Orders` (
  `OrderID` integer PRIMARY KEY,
  `StudentID` integer,
  `CustomerID` integer,
  `JobID` integer,
  `PriceSheetID` integer,
  `items` integer,
  `DatePlaced` timestamp,
  `TotalAmount` integer,
  `Status` varchar(255)
);

CREATE TABLE `Barcode` (
  `barcodeID` integer PRIMARY KEY,
  `pictures` integer
);

ALTER TABLE `Orders` ADD FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`);

ALTER TABLE `Orders` ADD FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`);

ALTER TABLE `Orders` ADD FOREIGN KEY (`PriceSheetID`) REFERENCES `PriceSheets` (`PriceSheetID`);

ALTER TABLE `Students` ADD FOREIGN KEY (`barcodeID`) REFERENCES `Barcode` (`barcodeID`);

ALTER TABLE `Orders` ADD FOREIGN KEY (`StudentID`) REFERENCES `Students` (`StudentID`);

ALTER TABLE `Photographers` ADD FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`);

ALTER TABLE `Students` ADD FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`);
