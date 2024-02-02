CREATE TABLE `Photographers` (
  `PhotographerID` integer PRIMARY KEY,
  `JobID` integer,
  `photographerfname` varchar(255),
  `photographerlname` varchar(255),
  `photographerContactNumber` varchar(255),
  `photographerEmail` varchar(255)
);

CREATE TABLE `Customers` (
  `CustomerID` integer PRIMARY KEY,
  `customerfname` varchar(255),
  `customerlname` varchar(255),
  `customerContactNumber` varchar(255),
  `customerEmail` varchar(255),
  `customerAddress` varchar(255)
);

CREATE TABLE `Jobs` (
  `JobID` integer PRIMARY KEY,
  `SchoolName` varchar(255),
  `pictureDate` timestamp,
  `schoolLocation` varchar(255),
  `schoolContactNumber` varchar(255),
  `schoolEmail` varchar(255),
  `schoolAddress` varchar(255)
);

CREATE TABLE `Students` (
  `StudentID` integer PRIMARY KEY,
  `fname` varchar(255),
  `lname` varchar(255),
  `teacher` varchar(255),
  `GradeOrClass` varchar(255),
  `barcodeID` integer,
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
  `CartID` integer,
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
